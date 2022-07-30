from bootstrap import db
from sqlalchemy import ARRAY, String


class Choices(db.Model):
    __tablename__ = 'choices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    choices = db.Column(ARRAY(String), nullable=False)
