from flask import Flask,render_template,request
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from .models import configure as configure_db
from .models.products import Product
from .models.serealizer import configure as configure_ma # configure_marshmallow
'''como rodar este app
export FLASK_APP=app   [ele vai procurar o arquivo app ou pasta app kcontem um __init__.py]
                e vai reconhecer o seu factory k devolve um app
export FLASK_DEBUG=True
export FLASK_ENV=Development

e ai so dar flask run  //flask db init {se ainda nao tem migrations} flask db migrate

'''

def create_app():
    app=Flask(__name__)
    app.config['DEBUG']=True
    #2 configurando o bootstrap
    Bootstrap(app)
    #3 configurando o database
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///storage/tables.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.config['SQLALCHEMY_BINDS']={'appmeta':'sqlite:///database/tables.db'}
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    # app.config['SQLALCHEMY_BINDS']={'appmeta':'sqlite:///db/storage.db'}
    #todo:[] 3.1. configure obanco primeiro e depois a migracao
    configure_db(app)
    #todo:[]3.2 configurando o marshmallow com ao meu app
    configure_ma(app)

    #todo[] 4: configurando migraceos do banco
    # Todo:  >> as configuracoes de migracao precisa primero k vc configure o banco primeiro e
    #5 configure o app,db e o directorio k por default este directorio ='migrations
    Migrate(app, app.db)  #intragando amigracao
    # after this run flask migration you can run in command line
    # flask db >> ele mostrara todas as opcoes disponives do banco [migrate, upgrate downgrate ...]
    #  e se for pra fazer a inicializacoa do banco
    # >> flask db init  [depois de ter  rodado isto ele vai gerar o apasta migrations mas
    #  tenha certeza que configurou o db configure_db(app)]
    #5.2. e depois se dar um [>> flask db migrate] ele ja vai criar o arquivo.db e as tabelas com uma versai
    # caso deseja modificar uma coluna ou sei la qualquer coisa numa tabela ou acresentar uma tabela
    # modifique seus models quanto quiser mas depois pra salva-los dê um [>>flask db migrate]
    
    
    #todo CONFIGURANDO OS MEUS BLUEPRINTS
    from .views.products import bp_product
    app.register_blueprint(bp_product, url_prefix='/product')
    
    from .views.books import nam, bp_book
    app.register_blueprint(bp_book, url_prefix='/book')
    
    # ''' esta é a forma de registar uma funcao que tem como rota ale de atribuir o decorador @app.route('/user<username>') '''
    # app.add_url_rule('/user/<username>', view_func=user_profile, endpoint='user', methods=['POST','GET'])
    app.add_url_rule('/', view_func =default, endpoint='/', methods=['get','post'])
    app.add_url_rule("/dashboard", view_func=dashboard, endpoint='/dashboard', methods=['GET','POST'])
    return app



def default():
    'routa sera definida de uma forma inteligente'
    print('Main Home it il go out now')
    print(request.method)
    return render_template('index.html')

def dashboard():
    'routa de dashboard'

    return render_template('home.html')


if __name__ == '__main__':
    app=create_app()
    app.run(debug=True, host='0.0.0.0')
    