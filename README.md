# flask_crud_main
passos principais pra fazer um CRUD no Flask
> ```flask_sqlalchemy ``` =- as dabtabse orm
> ```flask_migrate```  to migrate easly our database
> ```flask_marshmallow``` >> lib usado pra serializar as nossas tabelas de manera mais fácil

# COMO RODAR ESTE APP
```sh
export FLASK_APP=app
colacando em modo de desenvolvimento
export FLASK_ENV=Development
export FLASK_DEBUG=TRUE

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
 