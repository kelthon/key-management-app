'''
    Rota Principal

    add :  if session.get('autenticado',False)==False:
       return (redirect(url_for('login')))
'''
from typing import cast
from key_manager import app
from key_manager.models import db
from key_manager.forms.formLogin import Login
from key_manager.models.user import User
from key_manager.models.key import Key
from key_manager.models.news import News
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
        flash("Erro ao inicializar sqlite", "error_msg")
  
@app.route('/')
def index():
    news = News.query.order_by(News.date.desc()).all()
    return render_template('index.html', news=news, title="Gerenciador de Chaves UFCA KMAPP")

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<redic>', methods=['GET', 'POST'])
def login(redic='index'):
    if not session.get("user_auth", False) or session["user_auth"] == False:
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
                    account = request.form.get('account')
                    password = request.form.get('password')
                    # remenber = request.form.get('remenberMe')
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
                            session['user_name'] = user.name.split(' ')[0]
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
        return (render_template('forms/login.html', form=formLogin, action=url_for('login'), title="Entrar", hidden_footer=True))
    return redirect(url_for("index"))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'user_id' in session:
        session['user_id'] = None
        session['user_name'] = None
        session['user_username'] = None
        session['user_auth'] = False
        session['user_permission'] = 'normal'
    return redirect(url_for('index'))

@app.route('/config')
def config():
    if session.get("user_auth", False):
        return render_template("config/config.html", title="Configurações", hidden_footer=True)
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def notFound(error):
    return (render_template('notfound.html', title="Página não encontrada", hidden_footer=True))
