from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)

App.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4" % quote('Maiphan13082003')
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=App)

