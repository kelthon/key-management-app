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
    keys = Key.query.filter_by(key_avaliable=True).order_by(Key.name).all()
    cats = Category.query.order_by(Category.name).limit(7)
    regs = Registry.query.order_by(Registry.key_loan_date.desc()).limit(7)
    return render_template("view/indexView.html", keys=keys, categories=cats, registries=regs, key_names=Key.query, hidden_footer=True, title="Vizualização" )

@view.route("/category/<category_slug>")
def viewCat(category_slug): 
    category = Category.query.filter_by(slug=category_slug).first()
    
    if category is None:
        flash("Categoria não encontrada", "error_msg")
        return redirect(url_for("index"))

    keys = Key.query.filter_by(key_category_id=category.id).all()
    return render_template("view/categoryDetails.html", category=category, keys=keys, hidden_footer=True, title=category.name)

@view.route("/key/<key_slug>")
def viewKey(key_slug):    
    key = Key.query.filter_by(slug=key_slug).first()

    if key is None:
        flash("chave não encontrada", "error_msg")
        return redirect(url_for("index"))

    category = Category.query.filter_by(id=key.key_category_id).all()
    registry = Registry.query.filter_by(key_id=key.id).all()
    return render_template("view/keyDetails.html", key=key, categories=category, registry=registry, hidden_footer=True, title=key.name)

@view.route("/user/<user_username>")
def viewUser(user_username):
    
    user = User.query.filter_by(username=user_username).first()
    if user is None:
        flash("Usuário não encontrado", "error_msg")
        return redirect(url_for("index"))
    return render_template("view/users.html", user=user, hidden_footer=True, title=user.username)

@view.route("/registry/<reg_id>")
def viewReg(reg_id):
    registry = Registry.query.filter_by(id=reg_id).first()
    if registry is None:
        flash("Registro não encontrado", "error_msg")
        return redirect(url_for("index"))
    key = Key.query.filter_by(id=registry.key_id).first()
    user = User.query.filter_by(id=registry.user_id).first()
    return render_template("view/registryDetails.html", registry=registry, key=key, user=user, hidden_footer=True, title=f"Registro {registry.id}")

@view.route("/keys")
def viewAllKeys():    
    keys = Key.query.order_by("name").all()
    return render_template("view/keys.html", keys=keys, hidden_footer=True, title="Chaves")

@view.route("/categories")
def viewAllCategories():
    categories = Category.query.order_by("name").all()
    return render_template("view/categories.html", categories=categories, hidden_footer=True, title="Categorias")

@view.route("/registries")
def viewAllRegistries():
    registries = Registry.query.order_by(Registry.key_loan_date.desc()).all()
    key = Key.query
    user = User.query
    return render_template("view/registries.html", registries=registries, key=key, user=user, hidden_footer=True, title="Registros")

app.register_blueprint(view)