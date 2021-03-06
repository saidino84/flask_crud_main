from flask import Flask,render_template,request,jsonify,url_for
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from config import  config_app
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
s=URLSafeTimedSerializer('This is secret')
def create_app():
    app=Flask(__name__)
    
    s=URLSafeTimedSerializer('This is secret')
    # configurado as imformacoes do meu email
    app.config.from_pyfile('config.cfg')
    app.config['DEBUG']=True
    #2 configurando o bootstrap
    Bootstrap(app)
    mail=Mail(app)
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
    config_app(app)

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
    # modifique seus models quanto quiser mas depois pra salva-los d?? um [>>flask db migrate]
    
    
    #todo CONFIGURANDO OS MEUS BLUEPRINTS
    from .views.products import bp_product
    app.register_blueprint(bp_product, url_prefix='/product')
    
    from .views.books import nam, bp_book
    app.register_blueprint(bp_book, url_prefix='/book')
    
    # ''' esta ?? a forma de registar uma funcao que tem como rota ale de atribuir o decorador @app.route('/user<username>') '''
    # app.add_url_rule('/user/<username>', view_func=user_profile, endpoint='user', methods=['POST','GET'])
    app.add_url_rule('/', view_func =default, endpoint='/', methods=['get','post'])
    app.add_url_rule("/dashboard", view_func=dashboard, endpoint='/dashboard', methods=['GET','POST'])
    # app.add_url_rule('/login', view_func=login, endpoint='/login-page', methods=['POST','GET'])
    
    # return app


    @app.route('/login', methods=['POST','GET'])
    def login():

        print('Please login in to our page'+ request.method)
        if request.method=='POST':
            email=request.form['email']
            token=s.dumps(email, salt='email-confirm')

            # criando mesage para enviar 
            msg=Message('Cofirme o Email', sender='tylorguy2018@gmail.com', recipients=[email])
            link=url_for('confirm_token', token=token,external=True)
            msg.body='Your link is {}'.format(link)
            mail.send(msg)
            return jsonify({'dados':request.form.to_dict(),'token':token})
            
        return render_template('login.html')
    

    
    @app.route('/confirm_token/<token>')
    def confirm_token(token):
        try:
            email=s.loads(token, salt='email-confirm', max_age=50)
            return 'the token is steel working fine'
        except SignatureExpired as expirou:
            return '<h2> o token ja expirou</h2>'

        return 'The token is workingg'


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
    