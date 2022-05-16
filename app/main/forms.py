from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired 

class BlogForm(FlaskForm):
    blog_title = StringField('Blog Title', validators= [DataRequired()])
    blog_content = TextAreaField('Content', validators= [DataRequired()])
    submit= SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment_body =StringField('Comment', validators= [DataRequired()])
    submit= SubmitField('Submit')