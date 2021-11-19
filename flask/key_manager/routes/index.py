'''
    Rota Principal

    add :  if session.get('autenticado',False)==False:
       return (redirect(url_for('login')))
'''
from key_manager import app
from key_manager.models import db
from flask import (
    render_template,
    request, url_for, redirect, 
    flash, session
)

@app.before_first_request
def initialize():
    try:
        db.create_all()
    except:
        print("Erro ao inicializar sqlite")
        
@app.route('/')
def index():
    return (render_template('index.html'))

@app.route('/login')
def login():
    return (render_template('login.html'))

@app.route('/<notfound>')
def notFound(notfound):
    return (render_template('notfound.html'))

    