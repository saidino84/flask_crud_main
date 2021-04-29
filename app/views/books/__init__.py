'''blueprit de produtos 
rotas: /mostrar /atualiazr
'''
from flask import  Blueprint, render_template,request,url_for,jsonify, current_app
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
    return books.jsonify(result), 200 # outra ar é 200

@bp_book.route('/deletar/<id>', methods=['GET'])
def deletar(id):
    #todo deletar funciona normalment
    Book.query.filter(Book.id ==id).delete()
    current_app.db.session.commit()
    return jsonify({'delete':'sucessfull'}), 200
    ...

@bp_book.route('/modificar/<id>',methods=['GET','POST'])
def modificar(id):
    'Funcionou cara'
    print('Modificar '+id)
    book=Book.query.filter(Book.id ==id)
    book.update(request.json)
    current_app.db.session.commit()
    bs=BookSchema()
    return bs.jsonify(book.first())
    
@bp_book.route('/cadastrar', methods=['POST','GET'])
def cadastrar():
    bs=BookSchema()

    # dados={'autor':'saidino','name':'Live de Python'}
    #'''#todo Funciona Nomalmnt
    book=Book(name=request.json['name'], autor=request.json['autor'])
    # book, error=bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    print(book)
    print(f'Salvado com sucesso  {book.__dict__}')

    return jsonify(),201
    # '''

    '''#todo Tentando com serializacoa falha a serializaco
    bk, err=bs.load(request.json)
    print('load sucessfully and serializ')
    current_app.db.session.add(bk)
    current_app.db.session.commit()
    return bs.jsonify(bk) ,201 # como ele vai criar a response é 201
    # se for algo recebidp por 
    'from requests import post'
    # pos('localhost:5000/book/cadastrar', json={'nome':'book1', 'escritot':'tylor'}) 
    # seria:\
    #  book, error= bs.load(request.json)  [ aqui book ja foi serializado pra um tipo Book() do nosso model podemos ]
    #  current_app.db.session.add(book)\
    #  current_app.db.session.commit()

    # print(request.json())

    return bs.jsonify(book),200  
    '''
    #o BookShema tem um jsonify dele 
    '''
    dados={'autor':saidino,'title':'python book'}
    post('http://localhost:5000/book/cadastrar', json=dados).json()
    >>{'nome':saidino,'title':'python book'}

    '''


    ...