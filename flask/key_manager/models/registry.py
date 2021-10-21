'''
    Model de resgistro de movimentação das chaves
'''
from flask_sqlalchemy import SQLAlchemy

class Registry(db.model):
    __tablename__ = 'registries'
    