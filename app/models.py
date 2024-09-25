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
    # 关联UserDetails表
    details = db.relationship('UserDetails', backref=db.backref('user', uselist=False), uselist=False)

    def to_dict(self):
        # 包含UserDetails信息
        user_detail_dict = self.details.to_dict() if self.details else {}
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'is_delete': self.is_delete,
            'create_time': self.create_time,
            'update_time': self.update_time,
            'details': user_detail_dict
        }

    @classmethod
    def query_by_conditions(cls, **kwargs):
        """根据条件组合查询用户信息"""
        query = cls.query
        for key, value in kwargs.items():
            if value:
                query = query.filter(getattr(cls, key) == value)
        return query

    @classmethod
    def update_or_delete(cls, id, update_data=None, delete=False):
        """组合更新或删除用户信息"""
        user = cls.query.get(id)
        if not user:
            return None

        if update_data:
            for key, value in update_data.items():
                setattr(user, key, value)

        if delete:
            db.session.delete(user)

        db.session.commit()
        return user

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False, comment='用户ID')
    user_desc = db.Column(db.String(128), nullable=False, comment='用户描述')
    address = db.Column(db.String(128), nullable=True, comment='地址')
    user_type = db.Column(db.Integer, default=1, nullable=False, comment='用户类型')
    company = db.Column(db.String(64), nullable=True, comment='用户公司')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_desc': self.user_desc,
            'address': self.address,
            'user_type': self.user_type,
            'company': self.company
        }

    @classmethod
    def query_by_conditions(cls, **kwargs):
        """根据条件组合查询用户详细信息"""
        query = cls.query
        for key, value in kwargs.items():
            if value:
                query = query.filter(getattr(cls, key) == value)
        return query

    @classmethod
    def update_or_delete(cls, id, update_data=None, delete=False):
        """组合更新或删除用户详细信息"""
        detail = cls.query.get(id)
        if not detail:
            return None

        if update_data:
            for key, value in update_data.items():
                setattr(detail, key, value)

        if delete:
            db.session.delete(detail)

        db.session.commit()
        return detail