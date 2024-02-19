from wtforms import *
from wtforms.validators import *
from flask_wtf import *

class SignUpForm(FlaskForm):
    ID=DecimalField('ID',validators=[DataRequired()])
    name=StringField('name',validators=[DataRequired(),length(min=5,max=20)])
    age=StringField('age',validators=[DataRequired()])
    UID=StringField('UID',validators=[DataRequired(),length(min=10,max=10)])
    submit=SubmitField('Sign Up')
    
class LogInForm(FlaskForm):
    Username=StringField('Username',validators=[DataRequired(),length(min=5,max=20)])
    Password=PasswordField('Password',validators=[DataRequired(),length(min=5,max=20)])
    submit=SubmitField('Sign Up')