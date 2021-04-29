'''este arquio é serializador do/s meu/s modelos pra agente 
integrar no vetor das routas de uma maneira mais fácil

'''
from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelShema
from .products import Product
from .book import  Book

ma =Marshmallow()

def configure(app):
    'configuracoa de marshmellow ao meu app'
    ma.init_app(app)


#todo]: criar uma classe capaz de fazer as serializacao e deserializacoa
#todo]: de modelo que quizer mas pra meu caso é product 
#todo]: e faze -lo extender do Marshmallow().ModelSchema

#todo]: com marshmallow sera capaz receber um objecto que vem de 
#rota como json e transformar em um do nosso banco de dado

class ProductSchema(ma.Schema):
    'serializador de Product'
    class Meta:
        model =Product
        fields=('id','price','name','image_data','details','category')


'''\ colunas do modelo produtos\
    id =db.Column(db.Integer, primary_key=True)\
    price =db.Column(db.Integer)\
    name =db.Column(db.String)\
    image_data =db.Column(db.String)\
    details =db.Column(db.String)\
    category =db.Column(db.String)
'''

class BookSchema(ma.Schema):
    'serializer of books'
    class Meta:
        model =Book
        fields = ('id','name','autor')
