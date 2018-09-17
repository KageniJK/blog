from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Post, Comment, List
from flask_login import login_required, current_user
from .forms import PostForm, CommentForm
from .. import db, photos
from ..emails import notification


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
        recepients = List.get_emails()

        new_post = Post(title=title, post=post_actual, user_id=current_user.id)

        new_post.save_post()
        # notification("New blog post", "email/notification", recepients)
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


@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, post_id=post_id)

        new_comment.save_comment()

        return redirect(url_for('.post', post_id=post.id))

    comments = Comment.query.filter_by(post_id=post_id).all()

    return render_template('post.html', post=post, post_id=post_id, comment_form=form, comments=comments)