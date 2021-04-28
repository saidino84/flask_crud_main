from flask_sqlalchemy import SQLAlchemy
from . import  db #estou importando db no arquivo __init__



class Product(db.Model):
    '''esta tabela de produto contem como colunas:
    id, prece , name, 
    '''
    id =db.Column(db.Integer, primary_key=True)
    price =db.Column(db.Integer)
    name =db.Column(db.String)
    image_data =db.Column(db.String)
    details =db.Column(db.String)
    category =db.Column(db.String)


