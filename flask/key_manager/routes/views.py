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
    return "Views"

@view.route("/category/<category_slug>")
def viewCat(category_slug): 
    try:
        all_categories = Category.query.filter(Category.slug==category_slug).all()
    except:
        return render_template("categories.html")
    
    return render_template("categories.html", categories=all_categories)

@view.route("/key/<key_slug>")
def viewKey(key_slug):
    try:
        keyTeste = Key(id=1, name="Teste", slug="teste", key_category_id=1, key_avaliable=True)
        db.session.add(keyTeste)
        db.session.commit()
    except:
        pass
    try:
        all_keys = Key.query.filter_by(Key.slug==key_slug).all()
    except:
        return render_template("keys.html")
    
    return render_template("keys.html", keys=all_keys)

@view.route("/user/<username>")
def viewUser(username):
    try:
        userTeste = Key(id=1, name="Admin", username="Admin01", email="admin@admin.com", phone="+99 (99) 9 9999-9999", passwordd="12345", usertype="admin")
        db.session.add(userTeste)
        db.session.commit()
        all_users = User.query.filter_by(User.username==username).all()
        return render_template("users.html", keys=all_users)
    except:
        return render_template("users.html")

@view.route("/registry/<user_id>")
def viewReg(reg_id):
    try:
        all_registries = Registry.query.filter_by(Registry.id==reg_id).all()
        return render_template("registries.html", keys=all_registries)
    except:
        return render_template("registries.html")

@view.route("/<name>")
@view.route("/category")
@view.route("/key")
@view.route("/user")
@view.route("/registry")
def notFound(name):
    return "not found"

app.register_blueprint(view)