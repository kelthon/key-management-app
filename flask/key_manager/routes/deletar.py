from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.registry import Registry
from key_manager.models.news import News
from key_manager.forms.formUser import DelFormUser
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)
import hashlib
delete = Blueprint("delete", __name__, url_prefix="/del")

@delete.route('/category/<category_slug>')
def delCategory(category_slug):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        category = Category.query.filter_by(slug=category_slug).first()
        if category is None:
            flash("Categoria não encontrada", "error_msg")
        else:    
            db.session.delete(category)
            db.session.commit()
            flash("Categoria deletada com Sucesso", "success_msg")
        return redirect(url_for("view.viewIndex"))
    flash("Página não encontrada", "error_msg")
    return redirect(url_for("index"))

@delete.route('/key/<key_slug>')
def delKey(key_slug):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        key = Key.query.filter_by(slug=key_slug).first()
        if key is None:
            flash("Chave não encontrada", "error_msg")
        else:
            db.session.delete(key)
            db.session.commit()
            flash("Chave deletada com Sucesso", "success_msg")
        return redirect(url_for("view.viewIndex"))
    flash("Página não encontrada", "error_msg")
    return redirect(url_for("index"))
    
@delete.route('/user', methods=['GET', 'POST'])
def delUser():
    if session.get("user_auth", False) == True:
        delForm = DelFormUser()
        if request.method == 'POST':
            user_username = request.form.get('account')
            password = request.form.get('password')
            user_password = hashlib.md5(password.encode('utf8')).hexdigest()

            if session.get('user_username', False) != user_username:
                flash("Usuário incorreto", "error_msg")
                return redirect(url_for('delete.delUser'))
            else:
                user = User.query.filter_by(username=user_username, password=user_password).first()
                if user is None:
                    user = User.query.filter_by(email=user_username, password=user_password).first()
                if user is None:
                    flash("Senha Incorreta", "error_msg")
                    return redirect(url_for('delete.delUser'))
                else:
                    db.session.delete(user)
                    db.session.commit()
                    session['user_id'] = None
                    session['user_name'] = None
                    session['user_username'] = None
                    session['user_auth'] = False
                    session['user_permission'] = 'normal'
                    flash("Usuário deletado com Sucesso", "success_msg")
                return redirect(url_for("index"))
        return render_template("forms/delUser.html", form=delForm, action=url_for('delete.delUser'), hidden_footer=True, title="Deletar Usuário")
    flash("Página não encontrada", "error_msg")
    return redirect(url_for("index"))

@delete.route('/registry/<registry_id>')
def delRegistry(registry_id):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        registry = Registry.query.filter_by(id=registry_id).first()
        if registry is None:
            flash("Registro não encontrado", "error_msg")
        else:
            key = Key.query.filter_by(id=registry.key_id).all()
            key.key_avaliable = True
            db.session.delete(registry)
            db.session.commit()
            flash("Registro deletado com Sucesso", "success_msg")
        return redirect(url_for("view.viewIndex"))
    flash("Página não encontrada", "error_msg")
    return redirect(url_for("index"))

@delete.route('/news/<news_id>')
def delNews(news_id):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        news = News.query.filter_by(id=news_id).first()
        if news is None:
            flash("Notícia não encontrada", "error_msg")
            return redirect(url_for('index'))
        else:
            db.session.delete(news)
            db.session.commit()
            flash("Registro deletado com Sucesso", "success_msg")
    flash("Página não encontrada", "error_msg")
    return redirect(url_for("index"))

app.register_blueprint(delete)