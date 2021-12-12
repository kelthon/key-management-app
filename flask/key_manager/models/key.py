'''
    Model de cadastro das chaves

    O model das chaves, possui os campos de id, nome da chave, slug ou
    identificação da chave, categoria da chave: se e de bloco, armario, etc, e sua data de criação.
'''
from datetime import datetime
from key_manager.models import *

class Key(db.Model):
    __tablename__ = 'keys'
    id = db.Column(db.Integer, primary_key=True)
    key_category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    key_avaliable = db.Column(db.Boolean, default=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Key %r>' % self.name