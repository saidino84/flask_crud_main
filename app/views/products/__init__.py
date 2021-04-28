'''blueprit de produtos 
rotas: /mostrar /atualiazr
'''
from flask import  Blueprint, render_template,request,url_for,jsonify
from models.products import  product
from models.serealizer import ProductSchema



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
def cadastra():
    ...
