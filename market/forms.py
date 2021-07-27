from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField(label="User Name")
    email = StringField(label="Email:")
    password = StringField(label="Password:")
    confirmpassword = StringField(label="Confirm password:")
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    email = StringField(label="email")
    password = StringField(label="password")
    submit = SubmitField(label='Login')
