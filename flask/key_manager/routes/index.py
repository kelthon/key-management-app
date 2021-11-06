'''
    Rota Principal
'''
from key_manager import app
from key_manager.models import db

@app.before_first_request
def initialize():
    try:
        db.create_all()
    except:
        print("Erro ao inicializar sqlite")
        
@app.route('/')
def index():
    return "Seja Bem-vindo!"

@app.route('/<notfound>')
def notFound(notfound):
    return "Não encontrado!"
    