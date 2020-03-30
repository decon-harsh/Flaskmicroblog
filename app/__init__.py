from flask import Flask, render_template,url_for,flash,redirect,request
from forms import Registration,Login,Login_via_email
app = Flask(__name__)
app.config['SECRET_KEY']='795f58bed45eec911428443e6d6c6c77'
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
def hello_world():
    return render_template("Root.html")

@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/login',methods=['GET','POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        flash(f"Welcome {form.username.data},Long time no see!",'info')
        return redirect(url_for('home'))
    return render_template('login.html',form=form)
@app.route('/login_via_email',methods=['GET','POST'])
def login_via_email():
    form=Login_via_email()
    if form.validate_on_submit():
        flash(f"Welcome {form.email.data}, Long time no see!",'info')
        return redirect(url_for('home'))
    return render_template('login_via_email.html',form=form)   
@app.route('/register',methods=['GET','POST'])
def register():
    form=Registration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",form=form)    






if __name__ == "__main__":
    app.run(debug="TRUE") 