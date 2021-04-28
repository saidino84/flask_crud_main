'''blueprit de produtos 
rotas: /mostrar /atualiazr
'''
from flask import  Blueprint, render_template,request,url_for,jsonify
from app.models.products import  Product
from app.models.serealizer import ProductSchema

from app.models.book import Book
from app.models.serealizer import  BookSchema



bp_product =Blueprint('produtos',__name__)

@bp_product.route('/mostrar', methods=['GET'])
@bp_product.route('/',methods=['GET'])
def mostrar():
    'ENTRANDO NO BLUEPRINT DE PRODUTS'
    
    return render_template('home.html')

@bp_product.route('/deletar', methods=['DELETE'])
def deletar():
    ...

@bp_product.route('modificar',methods=['POST'])
def actualizar():
    ...
@bp_product.route('/cadastrar', methods=['POST'])
def cadastrar():
    ...
