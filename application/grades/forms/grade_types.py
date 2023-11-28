from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddGradeTypeForm(FlaskForm):
    pass

class UploadGradeTypesForm(FlaskForm):
    pass

class UpdateGradeTypeForm(AddGradeTypeForm):
    pass