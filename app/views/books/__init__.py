'''blueprit de produtos 
rotas: /mostrar /atualiazr
'''
from flask import  Blueprint, render_template,request,url_for,jsonify, current_app, redirect
from app.models.book import Book
from app.models.serealizer import  BookSchema



bp_book =Blueprint('books',__name__,static_folder='static',template_folder='templates')
nam='Saidino'

@bp_book.route('/',methods=['GET'])
@bp_book.route("/mostrar", methods=['GET','POST'])
def mostrar():
    result =Book.query.all()
    size=len(result)
    return render_template('bk_home.html', books=result,size=size), 200


@bp_book.route('/cadastrar', methods=['POST','GET'])
def cadastrar_livro():
    #todo cadastrar
    if request.method=='POST':
        form=request.form.to_dict();
        # return jsonify(form)
        book =Book(autor=form['book_autor'],name=form['book_name'])
        current_app.db.session.add(book)
        current_app.db.session.commit()
        print('Salvo com sucesso')
        return redirect(url_for('books.mostrar'))
    else:
        return render_template('add_book.html'), 200

@bp_book.route('/modify/<id>',methods=['POST','GET'])
def modificar(id):
    print('Modifyng')
    book=Book.query.filter(Book.id==id).first()
    print(book)
    if request.method=='POST':
        form=request.form.to_dict()
        for k,v in form.items():
            if v !=None and len(v)>=4:
                try:
                    book=Book.query.filter(Book.id==id)
                    book.update(form)
                    current_app.db.session.commit()
                    return 'Modificado com sucesso !'
                except Exception as err:
                    print(str(err))
                    return redirect(request.url)
            print('Falhou')
            return redirect(request.url)
        

    print('Getting back to HOme')
    return render_template('modificar.html',book=book )
    # print('Modificar '+id)
    # book=Book.query.filter(Book.id ==id)
    # book.update(request.json)
    # current_app.db.session.commit()
    # bs=BookSchema()
    # return bs.jsonify(book.first())





@bp_book.route('/deletar/<id>', methods=['GET'])
def deletar(id):
    #todo deletar funciona normalment
    Book.query.filter(Book.id ==id).delete()
    current_app.db.session.commit()
    return redirect(url_for('books.mostrar'))
    ...

class Valiadator:
    def __call__(name, autor):
        try:
            if name !=None or name.length<5:
                raise Exeption(f'{name} is invalid')
        except Exeption as err :
            print(str(err))
        finally:
            print(' thanks for the request')








'''
    USE FLUTTER TO 
    MANIPULE THESE FILES
    
    '''







#**************************************        #####
#      ####### ########        #    #########    #
#      #     #   #     #      #  #    #     #    #
# #### #     #   #     #     #    #   #     #    #
#      #     #   ######     ######## #######     #
#      #     #   #     #    #      #  #          #
#      #     #   #     #    #      #  #          #
# *    ####### #####   #  ####   #### ##      #######

@bp_book.route('/mostrar/api', methods=['GET'])
def mostrar_api():
    'ENTRANDO NO BLUEPRINT DE Book'
    
    books=BookSchema(many=True) #ele vai rederizar todos os campos de BookModel
    result =Book.query.all()
    jso=books.jsonify(result)
    #vai trazer alista em json dos books se tiver cadastrado
    return books.jsonify(result), 200 # outra ar é 200


@bp_book.route('/modificar_api/<id>',methods=['GET','POST'])
def modificar_api(id):
    'Funcionou cara'
    print('Modificar '+id)
    book=Book.query.filter(Book.id ==int(id))
    book.update(request.json)
    current_app.db.session.commit()
    bs=BookSchema()
    return bs.jsonify(book.first())

    # livro=Book()
@bp_book.route('/cadastrar_api', methods=['POST','GET'])
def cadastrar():
    bs=BookSchema()

    # dados={'autor':'saidino','name':'Live de Python'}
    #'''#todo Funciona Nomalmnt
    book=Book(name=request.json['name'], autor=request.json['autor'])
    book, error=bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    print(book)
    print('Salvado com sucesso  {book.__dict__}')

    return render_template('add_book.html'),201
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