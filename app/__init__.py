from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from .models import configure as configure_db
from .models.products import Product


'''como rodar este app
export FLASK_APP=app   [ele vai procurar o arquivo app ou pasta app kcontem um __init__.py]
                e vai reconhecer o seu factory k devolve um app
export FLASK_DEBUG=True
export FLASK_ENV=Development

e ai so dar flask run  //flask db init {se ainda nao tem migrations} flask db migrate

'''

def create_app():
    app=Flask(__name__)
    #2 configurando o bootstrap
    Bootstrap(app)
    #3 configurando o database
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///storage/tables.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    # app.config['SQLALCHEMY_BINDS']={'appmeta':'sqlite:///database/tables.db'}
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
    # app.config['SQLALCHEMY_BINDS']={'appmeta':'sqlite:///db/storage.db'}
    # 3.1. configure obanco primeiro e depois a migracao
    configure_db(app)
    #4: configurando migraceos do banco
    # Todo:  >> as configuracoes de migracao precisa primero k vc configure o banco primeiro e
    #5 configure o app,db e o directorio k por default este directorio ='migrations
    Migrate(app, app.db)
    # after this run flask migration you can run in command line
    # flask db >> ele mostrara todas as opcoes disponives do banco [migrate, upgrate downgrate ...]
    #  e se for pra fazer a inicializacoa do banco
    # >> flask db init  [depois de ter  rodado isto ele vai gerar o apasta migrations mas
    #  tenha certeza que configurou o db configure_db(app)]
    #5.2. e depois se dar um [>> flask db migrate] ele ja vai criar o arquivo.db e as tabelas com uma versai
    # caso deseja modificar uma coluna ou sei la qualquer coisa numa tabela ou acresentar uma tabela
    # modifique seus models quanto quiser mas depois pra salva-los dê um [>>flask db migrate]
    return app