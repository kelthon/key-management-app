'''
    Importa todos os módulos necessários,
    Configura a aplicação,
    e importa as rotas usadas no app
'''
from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, make_response, render_template
from flask import request, url_for, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import logging
import os

# Configuração do app, criptografia, db, bootstrap e CSRF
app = Flask(__name__) 
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////temp/KMApp.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

# Configuração do logging
logging.basicConfig(
    filename=CSV_DIR +  'app.log', filemode='w', 
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s', 
    level=logging.DEBUG
)

# Importação das rotas Rota 
from key_manager.routes import index 
from key_manager.routes import admin
