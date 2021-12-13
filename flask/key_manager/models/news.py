from datetime import datetime
from key_manager.models import *

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(150), nullable=True)
    content = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<News %r>' % self.id