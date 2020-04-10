from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User
import random

# suggestion function 
def suggestion(s):
    s=str(s)
    if s[-1].isdigit()==True:
        s=s[:len(s)-1]+str(int(s[-1])+1)
    else:
        s=s[:len(s)]+str(random.randint(0,10))
    return s

#forms
class Registration(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("Confirm your password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    
    #validations
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'''That username is taken please try another.\n You can try {suggestion(user.username)} as username''')         
    
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f"That email has already been registerd with us")
      


class Login(FlaskForm):
    username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    # email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    # confirm_password=PasswordField("Confirm your password",validators=[DataRequired(),EqualTo(password])])
    submit=SubmitField('Login')
    remember=BooleanField('remember me')


class Login_via_email(FlaskForm):
    # username=StringField("Username",validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    # confirm_password=PasswordField("Confirm your password",validators=[DataRequired(),EqualTo(password])])
    submit=SubmitField('Login')
    remember=BooleanField('remember me')    
