# flask_crud_main
Experiencia com um crud flask e suas feramentas
- Flask
- flask_sqlalchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlachemy

> ```flask_sqlalchemy ``` =- as dabtabse orm
> ```flask_migrate```  to migrate easly our database
> ```flask_marshmallow``` >> lib usado pra serializar as nossas tabelas de manera mais fácil ```to use it you have to isntall to > pipenv install marshmallow-sqlalchemy```

# COMO RODAR ESTE APP
```sh
export FLASK_APP=app
colacando em modo de desenvolvimento
export FLASK_ENV=Development
export FLASK_DEBUG=TRUE

como fazer as migracoes:
flask db init
flask db migrate
flask db upgrade

flask run --host=0.0.0.0
```


>  ``` Testando com requests do python ```

```python 
from requests import get ,post
```

# Flask MIgrate 
seria um lib de migracao de banco de dados com mais facilidade
> é fortemente recomendaddo que inicialize obanco no app antes de configurar as Migracoes e depois disto vem 

> * flask db init     basicamente pra inicializar o banco de dados
``` e é atraves deste comando que é gerado uma pasta migrations contendo tudo pra obanco```
- [x] se tentar rodar novamente flask db init vai dar erro dizendo k apasta migrations ja foi criado
 # e para Iniciar as migracoes agente precisa rodar o segundo comando

> * falsk db migrate  ```pra o arquivo de migracoes gerar aversao do banco ```

>tendo rodado o flask migrate noa] arquivo migration ja vai ser gerado um arquivo com nome stranho contendo as tabelas que criaste 
 e a primeira versao do banco k é 1; e se der um ``` caso quer modificar atabela uma coluna ou sei la qualquer coisa no database voce precisa dar um flask db migrate de novo assim ele vai gerar outro arquivo de versoa 2 contendo downgrade como o arquivo de versao 2 ``` ele  ja vai incrementar aversao do banco


 #Marshmellow
 > lib usado pra serializar os modelos de uma forma mais adequado

 ```py
from app.models.book import Book
from app.models.serealizer import  BookSchema
nam='saide'


bp_book =Blueprint('books',__name__, static_folder='static',template_folder='templates')

@bp_book.route('/mostrar', methods=['GET'])
@bp_book.route('/',methods=['GET'])
def mostrar():
    'ENTRANDO NO BLUEPRINT DE PRODUTS'
    
    books=BookSchema(many=True) #ele vai rederizar todos os campos de BookModel
    result =Book.query.all()
    jso=books.jsonify(result)
    #vai trazer alista em json dos books se tiver cadastrado
    return books.jsonify(result)

 ```