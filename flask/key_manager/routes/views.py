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
        cat = Category.query.filter_by(slug=category_slug).first()
        print(cat)
    except:
        return render_template("view/categories.html")
    
    return render_template("view/categories.html", categories=cat)

@view.route("/key/<key_slug>")
def viewKey(key_slug):
    try:
        keyTeste = Key(name="Teste", slug="teste", key_category_id=1, key_avaliable=True)
        print(keyTeste)
        db.session.add(keyTeste)
        db.session.commit()
    except:
        pass
    try:
        all_keys = Key.query.filter_by(slug=key_slug).all()
    except:
        return render_template("view/keys.html")
    
    return render_template("view/keys.html", keys=all_keys)

@view.route("/user/<username>")
def viewUser(username):
    try:
        userTeste = Key(name="Admin", username="Admin01", email="admin@admin.com", phone="+99 (99) 9 9999-9999", passwordd="12345", usertype="admin")
        db.session.add(userTeste)
        db.session.commit()
        all_users = User.query.filter_by(username=username).all()
        return render_template("view/users.html", keys=all_users)
    except:
        return render_template("view/users.html")

@view.route("/registry/<reg_id>")
def viewReg(reg_id):
    try:
        regTeste = Registry()
        db.session.add(regTeste)
        db.session.commit()
        all_registries = Registry.query.filter_by(id=reg_id).all()
        return render_template("view/registries.html", keys=all_registries)
    except:
        return render_template("view/registries.html")

@view.route("/<name>")
@view.route("/category")
@view.route("/key")
@view.route("/user")
@view.route("/registry")
def notFound(name):
    return "not found"

app.register_blueprint(view)