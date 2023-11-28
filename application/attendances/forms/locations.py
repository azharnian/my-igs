from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddLocationForm(FlaskForm):
    pass

class UploadLocationsForm(FlaskForm):
    pass

class UpdateLocationForm(AddLocationForm):
    pass