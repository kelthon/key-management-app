'''
    Importa todos os módulos necessários,
    Configura a aplicação,
    e importa as rotas usadas no app
'''
from flask import Flask, session
from flask_session.__init__ import Session
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import logging
import os

# Configuração do app, criptografia, db, bootstrap e CSRF
app = Flask(__name__) 

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
Session(app)
Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

# Conexão com db sqlite
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'key_manager/db/KMApp.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from key_manager.models import db
    db.init_app(app)
except:
    print("Erro ao conectar-se ao sqlite")

# Configuração do logging
logging.basicConfig(
    filename=CSV_DIR +  'app.log', filemode='w', 
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s', 
    level=logging.DEBUG
)

# Importação das rotas Rota 
from key_manager.routes import (
    index, admin, views, cadastro
)
