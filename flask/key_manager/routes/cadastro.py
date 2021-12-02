from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.registry import Registry
from key_manager.forms.formUser import FormUser
from key_manager.forms.formReg import RegForm
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)
import hashlib

cadastro = Blueprint("cadastro", __name__, url_prefix="/new")

@cadastro.route("/category")
def newCategory():
    return "new category"

@cadastro.route("/key", methods=["GET", "POST"])
def newKey():
    return "new key"

@cadastro.route("/user", methods=["GET", "POST"])
def newUser():
    userform = FormUser()
    
    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")

    if phone == "" or phone == None:
        phone = " "

    if userform.validate_on_submit():
        newuser = User(name=name, username=username, email=email, phone=phone, password=password)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("forms/cadastro_usuario.html", form=userform, action=url_for('cadastro.newUser'))

@cadastro.route('/registry', methods=['GET', 'POST'])
def newRegistry():
    regForm = RegForm()
    if request.method == "POST":
        user_id = request.form.get("user_name")
        loan_date = request.form.get("loan_date")
        return_date = request.form.get("return_date")
        key_id = request.form.get("key_id")
        name = request.form.get("name")
        email = request.form.get("email")
        
        if regForm.validate_on_submit():
            newRegistry = Registry(user_id=user_id, loan_date=loan_date, return_date=return_date, key_id=key_id, name=name, email=email)
            db.session.add(newRegistry)
            db.session.commit()
    
            return redirect(url_for("index"))
    return render_template("forms/cadastrar_emprestimo.html", form=regForm, action=url_for('cadastro.newRegistry'))

app.register_blueprint(cadastro)