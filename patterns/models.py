from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from patterns import db


class User(UserMixin, db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String,
        index=False, unique=True, nullable=False
    )

    password = db.Column(
        db.String(200),
        primary_key=False,
        unique=False,
        nullable=False
    )

    def set_password(self, password):
        """Create hashed password"""
        self.password = generate_password_hash(
            password
        )

    def check_password(self, password):
        """Check hashed password"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
