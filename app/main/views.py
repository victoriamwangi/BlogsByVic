
from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from ..models import User, Blog, Comment
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm

@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.posted.desc()).all()   
    
    return render_template('index.html', blogs=blogs) 

@main.route('/user/<uname>')
def profile(uname):
    user = current_user
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=uname)

@main.route('/user/<uname>/blogs/new', methods = ['GET', 'POST'])
@login_required
def new_blog(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
  
    form = BlogForm()

    if form.validate_on_submit():      
        new_blog = Blog(blog_title = form.blog_title.data, blog_content = form.blog_content.data, user_id = current_user.id)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    return render_template('new_blog.html', blog_form=form, user=uname )

@main.route('/add/<uname>/blogs/new')
@login_required
def add(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        return redirect(url_for('auth/login.html', uname=user.username))
            
    return render_template('comments.html')

@main.route('/blog/<int:blog_id>/new' , methods=['GET', 'POST'])
@login_required
def new_comment( blog_id):
    user = current_user.username
    blog = Blog.query.filter_by(id = blog_id).first()
    
    if user is None:
        return redirect(url_for('auth/login.html'))
        
    form = CommentForm()
    
    if form.validate_on_submit():
        new_comment = Comment(body = form.body.data, blog_id = blog, commenter = user)
        new_comment.save_comment()
        
        return redirect(url_for('index.html'))
    return render_template('comments.html', blog_form = form, user = user,blog = blog_id)