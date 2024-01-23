from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddCertificateForm(FlaskForm):
    awardee       = StringField("Name", validators=[DataRequired()])
    type          = StringField("Type", validators=[DataRequired()])
    level         = StringField("Level", validators=[DataRequired()])
    score         = IntegerField("Score", validators=[DataRequired()])
    online        = BooleanField('Online', validators=[DataRequired()], default = True)
    start_date    = DateField("Start", validators=[DataRequired()])
    expired_date  = DateField("End Date", validators=[DataRequired()])
    photo         = FileField('Certificate photo', validators=[DataRequired()])
    documentation = FileField('Documentation', validators=[DataRequired()])
    description   = StringField("Description", validators=[DataRequired()])
    submit        = SubmitField("Add")

class ReviseCertificate(FlaskForm):
    description   = StringField("Description", validators=[DataRequired()])
    submit        = SubmitField("Revise")

class UpdateCertificateForm(AddCertificateForm):
    description   = StringField("Description", validators=[DataRequired()])
    submit        = SubmitField("Update")
