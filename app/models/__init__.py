from flask_sqlalchemy import  SQLAlchemy

'''configuracoes de banco de dados '''

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db