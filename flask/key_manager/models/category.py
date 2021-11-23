'''
    Model de categorias

    Responsável por classificar as chaves. Ex.: Chaves de Blocos (BLOCO K, BLOCO J), 
    Chaves de Armário(Armário ADM), etc
    
    O model das categorias, possui os campos de id, nome da categoria, slug ou
    identificação da categoria, e sua data de criação.
'''
from datetime import datetime
from key_manager.models import *

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Category %r>' % self.name