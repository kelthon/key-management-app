'''
    Responsável por iniciar o servidor waitress
'''
from key_manager import app, serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/index')