
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import uuid
from app import db


roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'



class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dob = db.Column(db.Date)
    account_number = db.Column(db.String(64), unique=True)
    balance = db.Column(db.Float, default=0.0)
    user = db.relationship('User', backref=db.backref('customer', uselist = False), lazy=True)

    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'

class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    user = db.relationship('User', backref=db.backref('manager', uselist=False), lazy=True)

    def __repr__(self):
        return f'<Manager {self.first_name} {self.last_name}>'

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    user = db.relationship('User', backref=db.backref('admin', uselist=False), lazy=True)

    def __repr__(self):
        return f'<Admin {self.first_name} {self.last_name}>'

class AccountRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    status = db.Column(db.String(64))  # 'submitted', 'approved', 'rejected'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    customer = db.relationship('Customer', backref=db.backref('account_requests', lazy=True))

    def __repr__(self):
        return f'<AccountRequest {self.id}>'
