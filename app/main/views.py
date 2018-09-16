from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User
from flask_login import login_required, current_user
import markdown2
from .forms import PostForm


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """

    title = 'Mortus - Welcome to the blog'

    return render_template('index.html', title=title)

@main.route('/new_blog')
def new_blog():
    post_form = PostForm()
    # format_review = markdown2.markdown(blog,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('new_post.html', post_form=post_form)