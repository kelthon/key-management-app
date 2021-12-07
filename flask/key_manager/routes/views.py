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
    keys = Key.query.limit(10)
    cats = Category.query.limit(10)
    regs = Registry.query.limit(10)
    return render_template("view/indexView.html", keys=keys, categories=cats, registries=regs)

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

app.register_blueprint(view)