from flask import render_template
from models import Choices
from forms import ChoicesForm
from bootstrap import app, db


@app.route('/')
def index():
    form = ChoicesForm()
    return render_template('index.html', form=form)


@app.route('/', methods=['POST'])
def create_choices_submission():
    form = ChoicesForm()
    if form.validate_on_submit():
        try:
            choice = Choices(
              choices=form.choices.data
            )
            db.session.add(choice)
            db.session.commit()
            db.session.close()
            return render_template('index.html', form=form)
        except Exception as e:
            db.session.rollback()
            db.session.close()
            return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)
