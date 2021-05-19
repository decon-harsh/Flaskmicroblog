import secrets
import os,shutil
from PIL import Image
from flask import render_template,url_for,flash,redirect,request
from flaskblog import app,db,bcrypt,login_manager
from flaskblog.forms import Registration,Login,Login_via_email,suggestion,UpdateAccountForm,New_Post_Form
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required
#posts
posts=[
    {
        'author':"Harsh Singh",
        'title':"Blog post 1",
        'content':"First post content",
        'date':"April 28,2020"
    },
    {
        'author':"Harsh Singh",
        'title':"Blog post 2",
        'content':"Second post content",
        'date':"April 29,2020"
    },
    {
        'author':"Harsh Singh",
        'title':"Blog post 3",
        'content':"Third post content",
        'date':"April 30,2020"
    },
]








@app.route('/')
def Root():
    return render_template("Root1.html",title="Root Page")

@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home1.html',posts=posts,title="Home Page")
    else:
        flash(f"You have to Login first",'warning')
        return redirect(url_for("login"))

@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.remember.data)
                flash(f"Welcome {form.username.data},Long time no see!",'info')
                return redirect(url_for('home'))
            else:
                flash(f"Login Unsuccessful.Please check Username and Password",'danger')        
        else:
            flash(f"You do not have an account!","warning")
            
        # else:
            # flash(f"Login Unsuccessful.Please check Username and Password",'danger')        
    return render_template('login.html',form=form,title="Login")

@app.route('/login_via_email',methods=['GET','POST'])
def login_via_email():
    form=Login_via_email()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash(f"Welcome {user.username}, Long time no see!",'info')
            return redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful.Please check Email and Password",'danger')     
    return render_template('login_via_email.html',form=form,title="Login")   

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=Registration()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! \n You can now log in!",'success')
        # flash(f"You can now log in!",'success')
        return redirect(url_for('login'))        
    return render_template("register.html",form=form,title="Registration Page") 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Root'))


def save_picture(form_picture): 
    random_hex=secrets.token_hex(8)
    _ , f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static/image/profilepic',picture_fn)
    
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn




@app.route('/account',methods=['GET','POST'])
def account():
    if current_user.is_authenticated:
        form=UpdateAccountForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file=save_picture(form.picture.data)
                current_user.image_file= picture_file
            current_user.username=form.username.data
            current_user.email=form.email.data
            current_user.bio=form.bio.data
            db.session.commit()
            flash("Account has been updated",'success')
            return redirect(url_for('account'))
        elif request.method =='GET':
            form.username.data=current_user.username
            form.email.data=current_user.email   
            form.bio.data=current_user.bio     
        image_file=url_for('static',filename='image/profilepic/'+current_user.image_file)
        return render_template("account.html",title="Account",
                                    image_file=image_file,form=form)
    else:
        flash(f"You have to Login first",'warning')
        return redirect(url_for("login"))


@app.route('/new_post',methods=['GET','POST'])
def new_post():
    if current_user.is_authenticated:
        form=New_Post_Form()
        if form.validate_on_submit():
            Photo_filename=[]
            for files in form.Photo.data:
                save_picture(files)
            flash("Post Created!",'success')
            return redirect(url_for('home'))
        return render_template('New_Post.html',form=form,title="New Post")
    else:
        flash(f"You have to Login first",'warning')
        return redirect(url_for("login"))
    
