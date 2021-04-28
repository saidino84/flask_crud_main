# from  . from flask_sqlalchemy import SQLAlchemy
from . import  db


class Book(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(255))
    autor =db.Column(db.String(255))
