from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo 
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email Address', validators =[DataRequired(), Email()])
    username = StringField('Username', validators =[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Password Confirm', validators=[DataRequired(), EqualTo('Confirm Password', message='Password does not match')])
    submit = SubmitField('Sign Up')
    
    
  
    

    
    
