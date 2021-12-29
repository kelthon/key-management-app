'''
    Rota dos admnistradores
'''
from key_manager import app
from key_manager.models import db
from key_manager.models.key import Key
from key_manager.models.user import User
from key_manager.models.category import Category
from key_manager.models.registry import Registry
from key_manager.forms.formManager import ManagerForm
from flask import (
    Blueprint, render_template,
    request, url_for, redirect, 
    flash, session, make_response
)
from datetime import datetime

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def admHome():
    if session.get("user_permission", "normal") != "normal":
        return render_template("admin/indexAdmin.html", hidden_footer=True, title="Painel Administrativo")
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@admin.route("/manager", methods=['GET', 'POST'])
def manager_user_permissions():
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        users = User.query.filter_by(usertype='normal').all()
        managerForm = ManagerForm()
        if request.method == 'POST':
            user_username = request.form.get("username")
            user = User.query.filter_by(username=user_username)
            if user is None:
                flash("Usuário não encontrado", "error_msg")
                return redirect(url_for('admin.admHome'))
            user.usertype = 'admin'
            db.session.commit()
            flash("Usuário promovido com sucesso", "success_msg")
            return redirect(url_for('view.viewUser', user_username=user.username))
        return render_template("admin/gerenciarAdms.html", form= managerForm, action=url_for('admin.manager_user_permissions'), users=users, title="Gerenciar Permissões", hidden_footer=True)
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))

@admin.route('/return/<reg_id>')
def returnKey(reg_id):
    if session.get("user_auth", False) and session.get("user_permission", "normal") != "normal":
        registry = Registry.query.filter_by(id=reg_id).first()
        if registry is None:
            flash("Registro não encontrado", "error_msg")
            return redirect(url_for('admin.admHome'))
        key = Key.query.filter_by(id=registry.key_id).first()
        key.key_avaliable = True
        registry.key_return_date = datetime.utcnow()
        db.session.commit()
        flash("Registro atualizado com sucesso", "success_msg")
        return redirect(url_for('view.viewReg', reg_id=registry.id))
    flash("Página não encotrada", "error_msg")
    return redirect(url_for("index"))
    
app.register_blueprint(admin)