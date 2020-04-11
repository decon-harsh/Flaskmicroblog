from flask import render_template,url_for,flash,redirect,request
from flaskblog import app,db,bcrypt
from flaskblog.forms import Registration,Login,Login_via_email,suggestion
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user
#posts
posts=[
    {
        'author':"Harsh Singh",
        'title':"Blog post 1",
        'content':"First post content",
        'date':"April 28,2020"
    },
    {   
        'author':"Raju Madharchod",
        'title':"Vlog bnate hai",
        'content':"Yaar 9wa BT mat de",
        'date':"September 15,2020"
    },
    {
        'author':"9wa 9igga bosdike",
        'title':"Raghubar Das ki maa ka bhosda , Raghubar Das ki maa ki chut",
        'content':"Corona kiya hai",
        'date':"November 16,2020"
    },
    {
        'author':"Tumlog CM ko har baar bhul jata hai",
        'title':"Paisa kama liye be",
        'content':"Abe tumlog abhi tak golden rule nhi sikha hai",
        'date':"August 3,2020"
    },
    {
        'author':"Shubham Parteek Skp yo",
        'title':"Sonam(Hypo) chahiye yaar",
        'content':"Is this his life ?",
        'date':"November 20,2020"
    }
]








@app.route('/')
def Root():
    return render_template("Root1.html")

@app.route('/home')
def home():
    if current_user.is_authenticated:
        return render_template('home1.html',posts=posts)
    else:
        flash(f"You have to Login first",'warning')
        return redirect(url_for("login"))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form=Login()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash(f"Welcome {form.username.data},Long time no see!",'info')
            return redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful.Please check Username and Password",'danger')        
    return render_template('login.html',form=form)

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
    return render_template('login_via_email.html',form=form)   

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
        flash(f"Congratulations!")
        flash(f"Account created for {form.username.data}!",'success')
        flash(f"You can now log in!",'success')
        return redirect(url_for('login'))        
    return render_template("register.html",form=form) 

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Root'))