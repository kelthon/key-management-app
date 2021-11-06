'''
    Rota de Consulta
'''
from key_manager import app
from key_manager import db
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)

view = Blueprint("view", __name__, url_prefix="/view")

@view.route("/")
def index():
    return "Views"

@view.route("/category/<category_slug>")
def aviewReg(category_slug):
    try:
        all_categories = db.query.filter_by(category_slug).all()
        return render_template("categories.html", categories=all_categories)
    except:
        return "Nao encontrado"

@view.route("/key/<key_slug>")
def viewKey(key_slug):
    try:
        all_keys = db.query.filter_by(key_slug).all()
        return render_template("keys.html", keys=all_keys)
    except:
        return "Nao encontrado"

@view.route("/user/<username>")
def viewUser(username):
    try:
        all_users = db.query.filter_by(username).all()
        return render_template("users.html", keys=all_users)
    except:
        return "Nao encontrado"

@view.route("/registry/<user_id>")
def viewReg(reg_id):
    try:
        all_registries = db.query.filter_by(reg_id).all()
        return render_template("registries.html", keys=all_registries)
    except:
        return "Nao encontrado"

@view.route("/<name>")
@view.route("/category")
@view.route("/key")
@view.route("/user")
@view.route("/registry")
def notFound(name):
    return "not found"

app.register_blueprint(view)