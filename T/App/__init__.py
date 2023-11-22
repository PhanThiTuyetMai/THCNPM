from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

App = Flask(__name__)

App.secret_key = '*(nherhgnieor*nhtehmhbfg$$%%^$#%^&^%%'
App.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4" % quote('Admin@123')
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
App.config["PAGE_SIZE"] = 4

db = SQLAlchemy(app=App)
login = LoginManager(app=App)

