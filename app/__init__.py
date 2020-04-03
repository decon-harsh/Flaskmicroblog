from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from datetime import datetime

#Configs
app = Flask(__name__)
app.config['SECRET_KEY']='795f58bed45eec911428443e6d6c6c77'
app.config['SQLALCHEMY_DATAABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from app import routes
