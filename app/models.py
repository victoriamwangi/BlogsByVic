from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    pass_secure = db.Column(db.String())
    bio = db.Column(db.String())
    blogs = db.relationship('Blog', backref = 'users',passive_deletes=True, lazy= 'dynamic')
    # comments = db.relationship('Comment', backref='user', lazy="dynamic")
    
    
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
    

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key= True)
    blog_title = db.Column(db.String(255))
    blog_content = db.Column(db.String(4000))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    comments = db.relationship('Comment', backref = 'comment', lazy= 'dynamic')
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()
        
class Comment(db.Model):
    __tablename__ = 'comments'
    id= db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(100), nullable= False)
    commenter = db.Column(db.Integer, db.ForeignKey("users.id",ondelete='CASCADE'))
    timeposted = db.Column(db.DateTime, default=datetime.utcnow)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id',ondelete='CASCADE') )
    
    all_comments = []
  
    
    def save_comment(self):        
        db.session.add(self)
        db.session.commit()

        
    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(id=id).all()
        return comments
    
    @classmethod
    def get_comments(cls, id):

        response = []

        for comment in cls.all_comments:
            if comment.blog_id == id:
                response.append(comment)

        return response
