from flask_wtf import FlaskForm
from wtforms import (
    SelectMultipleField,
    SubmitField
)
from wtforms.validators import (
    DataRequired
)


choices = [
    ('choice1', 'choice1'),
    ('choice2', 'choice2'),
    ('choice3', 'choice3'),
    ('choice4', 'choice4')
]


class ChoicesForm(FlaskForm):
    choices = SelectMultipleField(
        'choices', validators=[DataRequired()],
        choices=choices
    )
    submit = SubmitField("Confirm Choices")
