'''
    Model de cadastro das chaves
'''
from flask_sqlalchemy import SQLAlchemy

class Key(db.model):
    __tablename__ = 'keys'
