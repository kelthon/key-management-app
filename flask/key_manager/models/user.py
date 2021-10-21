'''
    Model de usuarios
'''
from flask_sqlalchemy import SQLAlchemy

class User(db.model):
    __tablename__ = 'users'
