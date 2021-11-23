'''
    Model de usuarios

    O model de usuário possui os campos de id, nome completo, nome de usuário,
    email, telefone, senha, data de criação e permissões. 
'''
from datetime import datetime
from key_manager.models import *

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=True)
    password = db.Column(db.String(100), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ''' 
        Usertype pode ser Três master possui todas as permissões, 
        E admin possui menos permissões e normal não possui permissões
    '''
    usertype = db.Column(db.String(6), default="normal")
    def __repr__(self) -> str:
        return '<User %r>' % self.name