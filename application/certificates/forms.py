from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddCertificateForm(FlaskForm):
    awardee       = StringField("Name", validators=[DataRequired()])
    online        = BooleanField('Online', validators=[DataRequired()], default = True)
    type          = StringField("Type", validators=[DataRequired()])
    level         = StringField("Level", validators=[DataRequired()])
    score         = IntegerField("Score", validators=[DataRequired()])
    description   = StringField("Short Description", validators=[DataRequired()])
    submit        = SubmitField("Submit")


class UpdateCertificateForm(AddCertificateForm):
    description   = StringField("Short Description", validators=[DataRequired()])
    submit        = SubmitField("Submit")
