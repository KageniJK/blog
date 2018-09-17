from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class PostForm(FlaskForm):
    title = StringField('Post title', validators=[Required()])
    post = TextAreaField('Blog post')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField('Say something about this', validators=[Required()])
    submit = SubmitField('Submit')


class MailingForm(FlaskForm):
    email = StringField('email',validators=[Required()])
    submit = SubmitField('Join')