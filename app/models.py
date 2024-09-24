# models.py
from .db import db
from datetime import datetime

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    is_delete = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'is_delete': self.is_delete,
            'create_time': self.create_time,
            'update_time': self.update_time
        }


