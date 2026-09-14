from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):

    name = StringField(
        'What is your name?',
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')


class UserForm(FlaskForm):

    # Campo para digitar o nome do usuário
    username = StringField(
        'What is your name?',
        validators=[DataRequired()]
    )

    # Campo para escolher a função
    #
    # O valor recebido pelo formulário será convertido
    # para inteiro por causa do coerce=int.
    #
    # Exemplo:
    # Administrator -> 1
    # Moderator     -> 2
    # User          -> 3
    role = SelectField(
        'Role?:',
        coerce=int,
        validators=[DataRequired()]
    )

    # Botão de envio
    submit = SubmitField('Submit')


class RoleForm(FlaskForm):

    name = StringField(
        'Role Name',
        validators=[DataRequired()]
    )

    submit = SubmitField('Submit')