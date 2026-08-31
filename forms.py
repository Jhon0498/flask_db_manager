from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    """
    Form for simple name submission, matching the main page interface.
    """
    # Name input field with mandatory text requirement
    name = StringField('What is your name?', validators=[DataRequired()])
    # Form submission button
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    """
    Form for registering and managing users with an assigned role.
    """
    # Username input field with required validation
    username = StringField('Username', validators=[DataRequired()])
    # Dynamic dropdown for selecting the associated role ID
    # coerce=int ensures the submitted value is converted to an integer for SQLite Foreign Keys
    role = SelectField('Role', coerce=int)
    # Form submission button
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):
    """
    Form for creating new user roles/permissions.
    """
    # Role name input field
    name = StringField('Role Name', validators=[DataRequired()])
    # Form submission button
    submit = SubmitField('Submit')