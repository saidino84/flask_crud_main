from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from .models.products import configure as configure_db


def create_app():
    app=Flask(__name__)
    #2 configurando o bootstrap
    Bootstrap(app)
    #3 configurando o database
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///storage/db/tables.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_BINDS']={'appmeta':'sqlite:///storage/db/tables.db'}

    #4: configurando migraceos do banco
    # Todo:  >> as configuracoes de migracao precisa primero k vc configure o banco primeiro e
    # configure o app,db e o directorio k por default este directorio ='migrations
    Migrate(app, app.db)
    # after this run flask s
    return app