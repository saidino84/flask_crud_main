from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Produto(db.Model):
    '''esta tabela de produto contem como colunas:
    id, prece , name, 
    '''
    id =db.Column(db.Integer, primary_key=True)
    price =db.Column(db.Integer)
    name =db.Column(db.String)
    image_data =db.Column(db.String)
    description =db.Column(db.String)

