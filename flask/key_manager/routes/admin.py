'''
    Rota dos admnistradores
'''
from key_manager import app
from key_manager.models import db
from key_manager.models.category import Category
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.registry import Registry
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session
)

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def admHome():
    return (u"Administração")
@admin.route("/new/key", methods=["GET", "POST"])
def newKey():
    return "new key"

@admin.route('/cadastrar_usuario', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        date = request.form.get("date")
        level = request.form.get("level")
        if name and username and email and phone and password and date and level:
            r = User(name, username, email, phone, password, date, level)
            db.session.add(r)
            db.session.commit()
            
    return redirect(url_for("/"))
    
@admin.route('/cadastrar_emprestimo', methods=['GET', 'POST'])
def lend():
    if request.method == "POST":
        user_id = request.form.get("user_name")
        loan_date = request.form.get("loan_date")
        return_date = request.form.get("return_date")
        key_id = request.form.get("key_id")
        name = request.form.get("name")
        email = request.form.get("email")
        
        if user_id and loan_date and return_date and key_id and name and name and email:
            c = Registry(user_id, loan_date, return_date, key_id, name, email)
            db.session.add(c)
            db.session.commit()
    
    return redirect(url_for("index"))

app.register_blueprint(admin)