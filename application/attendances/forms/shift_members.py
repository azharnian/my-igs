from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddShiftMembersForm(FlaskForm):
    pass

class UploadShiftMembersForm(FlaskForm):
    pass

class UpdateShiftMembersForm(AddShiftMembersForm):
    pass