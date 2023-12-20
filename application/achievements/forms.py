from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, DateTimeField, DateField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddAchievementForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    organizer = StringField("Organized by", validators=[DataRequired()])
    description = TextAreaField("Description")
    category = StringField("Category", validators=[DataRequired()])
    online = BooleanField('Online', validators=[DataRequired()], default = False)
    comp_date = DateTimeField("Competition Date", validators=[DataRequired()])
    start_date = DateTimeField("Start Date", validators=[DataRequired()])
    end_date = DateTimeField("End Date", validators=[DataRequired()])
    submit = SubmitField("Add Achievement")

class UpdateAchievementForm(AddAchievementForm):
    submit = SubmitField("Update Achievement")

