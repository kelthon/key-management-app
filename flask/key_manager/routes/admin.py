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
    return render_template("admin/indexAdmin.html")

app.register_blueprint(admin)