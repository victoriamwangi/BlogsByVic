
from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from .. import db
from ..models import User, Blog, Comment
from flask_login import login_required, current_user
from .forms import BlogForm, CommentForm
# from ..request import get_blogQuotes




@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.posted.desc()).all()   
    # blogQuote= get_blogQuotes('')
    # blogQuote = get_blogQuotes()
    return render_template('index.html', blogs=blogs ) 
# blogQuote= blogQuote

@main.route('/user/<uname>')
def profile(uname):
    user = current_user
    blogs = Blog.query.filter_by(user_id = current_user.id).all()
    
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=uname, blogs= blogs)

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

        return redirect(url_for('.index', uname=user.username))
    return render_template('new_blog.html', blog_form=form, user=uname )

@main.route('/add/<uname>/blogs/new')
@login_required
def add(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        return redirect(url_for('auth/login.html', uname=user.username))
            
    return render_template('comments.html')

@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.get_or_404(id)
    if blog.user_id != current_user.id:
        return render_template('errors/403.html')
    db.session.delete(blog)
    db.session.commit()
 
    return redirect (url_for('main.index' ))
@main.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    comment =Comment.query.get_or_404(comment_id)
    if (comment.commenter) != current_user.id:
        abort(403)
    db.session.delete(comment)
    db.session.commit()
    flash('The comment has been deleted!')
    return redirect (url_for('main.index'))#h

    
@main.route('/view/<int:id>', methods=['GET', 'POST'])
@login_required
def view_blog(id):
    blog = Blog.query.get_or_404(id)
    blog_comments = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    user = current_user.id
    if comment_form.validate_on_submit():
        
        new_comment = Comment(blog_id=id, body=comment_form.body.data, commenter=user)
        new_comment.save_comment()
         
    return render_template('view_blog.html', blog=blog, blog_comments=blog_comments, comment_form=comment_form)




@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    blog = Blog.query.get_or_404(id)
    if blog.user_id != current_user.id:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        blog.blog_title = form.blog_title.data
        blog.blog_content = form.blog_content.data
        db.session.commit()

        return redirect(url_for('main.index'))#h
    elif request.method == 'GET':
        form.blog_title.data = blog.blog_title
        form.blog_content.data = blog.blog_content
    return render_template('update.html', blog_form=form)


