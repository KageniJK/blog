from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Post
from flask_login import login_required, current_user
import markdown2
from .forms import PostForm
from .. import db, photos


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """
    posts = Post.get_posts()
    title = 'Mortus - Welcome to the blog'

    return render_template('index.html', title=title, posts=posts)


@main.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    """
    Displays the new post page with a markdown form
    :return:
    """
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        post_actual = post_form.post.data

        new_post = Post(title=title, post=post_actual, user_id=current_user.id)

        new_post.save_post()
        return redirect(url_for('.profile', uname=current_user.username))

    return render_template('new_post.html', post_form=post_form)


@main.route('/user/<uname>')
def profile(uname):
    """
    display user profiles
    :param uname:
    :return:
    """
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    posts = Post.query.filter_by(user_id=user.id).all()

    return render_template("profile/profile.html", user=user, posts=posts)


@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user= User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar = path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))


@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()

    return render_template('post.html', post=post)