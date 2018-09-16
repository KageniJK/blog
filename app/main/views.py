from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Post
from flask_login import login_required, current_user
import markdown2
from .forms import PostForm


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """
    posts = Post.get_posts()
    title = 'Mortus - Welcome to the blog'

    return render_template('index.html', title=title, posts=posts)


@main.route('/new_blog')
def new_blog():
    """
    Displays the new post page with a markdown form
    :return:
    """
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        post = post_form.post.data

        new_post = Post(title=title, post=post, user_id=current_user.id)

        new_post.save_post()
        return redirect(url_for('.post', id=post.id))

    return render_template('new_post.html', post_form=post_form)