from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db
from ..models import User
from flask_login import login_required, current_user


@main.route('/')
def index():
    return(render_template('index.html'))

@main.route('/user/<uname>')
def profile(uname):
    user = current_user
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=uname)