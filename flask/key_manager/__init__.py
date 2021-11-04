'''
    Importa todos os módulos necessários,
    Configura a aplicação,
    e importa as rotas usadas no app
'''
from flask import Flask
from waitress import serve
from flask import jsonify, make_response, render_template
from flask import request, url_for, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import logging
import os

# Configuração do app, criptografia, db, bootstrap e CSRF
app = Flask(__name__) 

app.config['SECRET_KEY'] = os.urandom(24)
bootstrap = Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

# Conexão com db sqlite
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/KMApp.db'
    from models import db
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
from key_manager.routes import *
