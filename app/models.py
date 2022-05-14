from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String())
    bio = db.Column(db.String())
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the passoword attribute')
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password )
    
    def __repr__(self):
        return f'User{self.username}'