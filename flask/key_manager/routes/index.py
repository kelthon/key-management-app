'''
    Rota Principal
'''
from key_manager import app

@app.route('/')
def index():
    return "Seja Bem-vindo!"
    