from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMPANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    resume = db.Column(db.String(256))
    company = db.relationship('Company', uselist=False, back_populates='user')

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_company(self):
        return self.role == self.ROLE_COMPANY


class Position(Base):
    __tablename__ = 'position'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    description = db.Column(db.String(256))
    salary = db.Column(db.String(64))
    brief = db.Column(db.String(128))
    requirement = db.Column(db.String(128))
    company = db.relationship('Company', uselist=False)

    def __repr__(self):
        return '<Position:{}>'.format(self.name)


class Company(Base):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    logo_url = db.Column(db.String(256))
    website = db.Column(db.String(128), unique=True)
    logline = db.Column(db.String(128))
    site = db.Column(db.String(128))
    position = db.relationship('Position')
    user = db.relationship('User', back_populates='company')

    def __repr__(self):
        return '<Company:{}>'.format(self.name)
