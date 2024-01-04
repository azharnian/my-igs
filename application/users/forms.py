from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Optional, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

class UserLoginForm(FlaskForm):
    username = StringField("User ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class AddUserForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(min = 4)])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min = 4)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min = 4)])
    username = StringField("Username", validators=[DataRequired(), Length(min = 4)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min = 8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message = "Password must match!")])
    submit = SubmitField("Add User")

class UpdateUserForm(AddUserForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 4)])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(min = 4)])
    submit = SubmitField("Update User")

class SearchUserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 4)])
    submit = SubmitField('Search')