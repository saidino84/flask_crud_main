

def config_email(app):
    app.config['DEBUG']=True
    app.config['MAIL_SERVER']='smtp.hushmail.com'
    app.config['MAIL_PORT']=587
    app.config['MAIL_USE_TLS']=True
    app.config['MAIL_USE_SSL']=False
    # app.config['MAIL_DEBUG']=True
    app.config['MAIL_USERNAME']='saideadamadam@gmail.com'
    app.config['MAIL_PASSWORD']='clausaidino'
    app.config['MAIL_DEFAULT_SENDER']='clausadidino@gmail.com'
    app.config['MAIL_MAX_EMAILS']=None
    # app.config['MAIL_SUPRESS_SEND']=False
    app.config['MAIL_ASCII_ATTACHMENTS']=True
