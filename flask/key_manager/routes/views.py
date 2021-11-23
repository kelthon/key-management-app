'''
    Rota de Consultas
'''
from key_manager import app
from key_manager import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.registry import Registry
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)

view = Blueprint("view", __name__, url_prefix="/view")

@view.route("/")
def viewIndex():
    return (
    "<h1>Views</h1><br><a href='/view/category/categoria-teste-1'>Categorias</a><br><a href='/view/key/chave-teste-1'>Chaves</a><br><a href='/view/user/AdminMaster01'>Users</a><br><a href='/view/registry/1'>RGs</a><br><button><a href='/view/init'>Criação rápida</button></a>"
    )

@view.route("/category/<category_slug>")
def viewCat(category_slug): 
    try:
        category = Category.query.filter_by(slug=category_slug).first()
    except:
        pass
    
    return render_template("view/categories.html", category=category)

@view.route("/key/<key_slug>")
def viewKey(key_slug):    
    try:
        keys = Key.query.filter_by(slug=key_slug).first()
    except:
        pass
    return render_template("view/keys.html", key=keys)

@view.route("/user/<user_username>")
def viewUser(user_username):
    try:
        all_users = User.query.filter_by(username=user_username).first()
    except:
        pass
    return render_template("view/users.html", user=all_users)

@view.route("/registry/<reg_id>")
def viewReg(reg_id):
    all_registries = Registry.query.filter_by(id=reg_id).all()
    return render_template("view/registries.html", registries=all_registries)

@view.route("/init")
def init():
    cat = Category(name="Categoria Teste 1", slug="categoria-teste-1")
    key = Key(key_category_id=1, name="Chave Teste 1", slug="chave-teste-1")
    user = User(name="Jão Admin", username="AdminMaster01", email="jão@admin.com", password="12345", phone="+99 (99) 9 9999-9999", usertype="admin")
    reg = Registry(user_id=1, key_id=1, holder_name="unknow", holder_email="unknow@unknow.com")

    try:
        db.session.add(cat)
        db.session.add(key)
        db.session.add(user)
        db.session.add(reg)

        db.session.commit()
    except:
        pass

    return redirect(url_for('view.viewIndex'))

@view.route("/<name>")
@view.route("/category")
@view.route("/key")
@view.route("/user")
@view.route("/registry")
def notFound(name):
    return "<h1>Not found</h1><br><a href='/view/'>Click here to back</a>"

app.register_blueprint(view)