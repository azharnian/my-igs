from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField,DateField
from wtforms.validators import DataRequired, Optional
from flask_wtf.file import FileField, FileAllowed

class AddAchievementForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    organizer = StringField("Organized by", validators=[DataRequired()])
    description = TextAreaField("Description")
    category = StringField("Category", validators=[DataRequired()])
    online = BooleanField('Online', validators=[DataRequired()], default = False)
    comp_date = DateField("Competition Date", validators=[DataRequired()])
    start_date = DateField("Start", validators=[DataRequired()])
    end_date = DateField("End Date", validators=[DataRequired()])
    photo = FileField('Achievement Photo', validators=[DataRequired()])
    documentation = FileField('Documentation', validators=[DataRequired()])
    submit = SubmitField("Add")

class UpdateAchievementForm(AddAchievementForm):
    submit = SubmitField("Update")

class AddRevisionForm(FlaskForm):
    achievement_id = IntegerField("Achievement ID", validators=[DataRequired()])
    comment_content = TextAreaField("Comment", validators=[DataRequired()])
    comp_date_revision = DateField("Revised Competition Date", validators=[Optional()])
    start_date_revision = DateField("Revised Start Date", validators=[Optional()])
    end_date_revision = DateField("Revised End Date", validators=[Optional()])
    submit = SubmitField("Add Revision")
