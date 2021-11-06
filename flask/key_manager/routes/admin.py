'''
    Rota dos admnistradores
'''
from key_manager import app
from flask import Blueprint

admin = Blueprint("admin", __name__, url_prefix="/admin")

@admin.route("/")
def admHome():
    return (u"Administração")
@admin.route("/new/key", methods=["GET", "POST"])
def newKey():
    return "new key"

app.register_blueprint(admin)