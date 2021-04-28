'''blueprit de produtos 
rotas: /mostrar /atualiazr
'''
from flask import  Blueprint, render_template,request,url_for,jsonify

from app.models.book import Book
from app.models.serealizer import  BookSchema



bp_book =Blueprint('books',__name__,static_folder='static',template_folder='templates')
nam='Saidino'


@bp_book.route('/mostrar', methods=['GET'])
@bp_book.route('/',methods=['GET'])
def mostrar():
    'ENTRANDO NO BLUEPRINT DE Book'
    
    books=BookSchema(many=True) #ele vai rederizar todos os campos de BookModel
    result =Book.query.all()
    jso=books.jsonify(result)
    #vai trazer alista em json dos books se tiver cadastrado
    return books.jsonify(result)

@bp_book.route('/deletar', methods=['DELETE'])
def deletar():
    ...

@bp_book.route('modificar',methods=['POST'])
def actualizar():
    ...
@bp_book.route('/cadastrar', methods=['POST'])
def cadastrar():
    ...