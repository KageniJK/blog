from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required, current_user


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """

    title = 'Home - Pitch'

    return render_template('index.html', title=title)

