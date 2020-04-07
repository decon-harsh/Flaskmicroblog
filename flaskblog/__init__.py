from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from datetime import datetime

#Configs
app = Flask(__name__)

app.config['SECRET_KEY']='795f58bed45eec911428443e6d6c6c77'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)

from flaskblog import routes
