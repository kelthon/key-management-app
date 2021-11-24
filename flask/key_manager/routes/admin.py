'''
    Rota dos admnistradores
'''
from key_manager import app
from key_manager.models import db
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

@admin.route('/cadastrar_usuario', methods['GET', 'POST'])
def cadastrar
    if request.method == "POST"
        user_id = request.form.get("user_name")
        loan_date = request.form.get("loan_date")
        return_date = request.form.get("return_date")
        key_id = request.form.get("key_id")
        name = request.form.get("name")
        email = request.form.get("email")
        
        if user_id and loan_date and return_date and key_id and name and name and email:
            r = Registry(user_id, loan_date, return_date, key_id, name, email)
            db.session.add(r)
            db.session.commit()
    
    return redirect(url_for("index"))

app.register_blueprint(admin)