
from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from ..models import User, Blog
from flask_login import login_required, current_user
from .forms import BlogForm

@main.route('/')
def index():
    return(render_template('index.html'))

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
        new_blog = Blog(blog_title = form.blog_title.data, blog_content = form.blog_content.data)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))
    return render_template('new_blog.html', blog_form=form, user=uname )


@main.route('/blogs')
@login_required
def  allblogs():
    blogs = Blog.query.all()
    
    return render_template('all_blogs.html', blogs= blogs)
    
