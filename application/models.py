from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

    __tablename__ = 'login-users'

    id = db.Column(
        db.Integer,
        primary_key = True
    )
    name = db.Column(
        db.String(60),
        unique=True,
        nullable=True
    )
    email = db.Column(
        db.String(60),
        unique=True,
        nullable=True
    )
    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )
    created = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
    last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    def set_password(self, password):
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.name