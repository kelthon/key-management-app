'''
    Rota Principal

    add :  if session.get('autenticado',False)==False:
       return (redirect(url_for('login')))
'''
from key_manager import app
from key_manager.models import db
from key_manager.forms.formLogin import Login
from key_manager.models.user import User
from flask import (
    render_template,
    request, url_for, redirect, 
    flash, session
)
import hashlib

@app.before_first_request
def initialize():
    try:
        db.create_all()
    except:
        print("Erro ao inicializar sqlite")
        
@app.route('/')
def index():
    return (render_template('index.html'))

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<redic>', methods=['GET', 'POST'])
def login(redic='index'):
    formLogin = Login()
    if session.get("secure_login_mode", False):
        flash("Você falhou em muitas tentativas de login espere um pouco antes de poder tentar novamente", "warning_msg")
    else:
        if session.get("login_attempts", False):
            if session["login_attempts"] > 5:
                flash("Você solicitou muitas requisições de login aguarte um tempo antes de submete-las novamente", "warning_msg")
                session["secure_login_mode"] = True
        if request.method == 'POST':
            if formLogin.validate_on_submit():
                account = request.form['account']
                password = request.form['password']
                # remenber = request.form['remenberMe']

                hash_password = hashlib.md5(password.encode("utf8")).hexdigest()

                try:
                    user = User.query.filter_by(email=account, password=hash_password).first()
                    if user is None:
                        user = User.query.filter_by(username=account, password=hash_password).first()
                    if user is None:
                        flash("Falha de autenticação", "error_msg")
                        existEmail = User.query.filter_by(email=account).first()
                        existUsername = User.query.filter_by(username=account).first()

                        if existEmail is None and existUsername is None:
                            flash("Conta Inexistente", "error_msg")
                        else:
                            flash("Senha Incorreta", "error_msg")
                        if session.get("login_attempts", False):
                            session["login_attempts"] += 1
                        else:
                            session["login_attempts"] = 1
                        return redirect(url_for('login'))
                    # if remenber:
                    try:
                        session['user_id'] = user.id
                        session['user_username'] = user.username
                        session['user_auth'] = True
                        session['user_permission'] = user.usertype
                        session["login_attempts"] = 0
                        flash("Usuário Logado com Sucesso", "success_msg")
                        return redirect(url_for(redic))
                    except:
                        flash("Falha de autenticação da Sessão", "error_msg")
                        return redirect(url_for('login'))
                except:
                    flash("Um erro inesperado ocorreu", "error_msg")
                    return redirect(url_for('login'))

    return (render_template('forms/login.html', form=formLogin, action=url_for('login'), hidden_footer=True))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user_id' in session:
        session['user_id'] = ''
        session['user_username'] = ''
        session['user_auth'] = False
        session['user_permission'] = 'normal'
    return redirect(url_for('index'))

@app.route('/<notfound>')
def notFound(notfound):
    return (render_template('notfound.html', hidden_footer=True))
