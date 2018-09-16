from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User



class PostForm(FlaskForm):

 title = StringField('Review title',validators=[Required()])

 review = TextAreaField('Movie review')

 submit = SubmitField('Submit')