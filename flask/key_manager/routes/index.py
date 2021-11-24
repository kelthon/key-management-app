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

@app.route('/formulario', methods['GET', 'POST'])
def cadastrar
    if request.method == "POST"
        user_id = request.form.get("user_name")
        loan_date = request.form.get("loan_date")
        return_date = request.form.get("return_date")
        key_id = request.form.get("key_id")
        name = request.form.get("name")
        email = request.form.get("email")
        
        if user_id and loan_date and return_date and key_id and name and name and email:
            r = Registry(user_id, loan_date, return_date, key_id, name, email)
            db.session.add(r)
            db.session.commit()
    
    return redirect(url_for("index"))