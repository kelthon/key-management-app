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

# rotas
@app.route('/')
def index():
    return "Bem-vindo!"

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/index')
    