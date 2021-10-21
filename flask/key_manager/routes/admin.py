'''
    Rota dos admnistradores
'''
from key_manager import app
from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin", template_folder='./templates/admin/')

@admin.route("/")
def admHome():
    return (u"Administração")

app.register_blueprint(admin)