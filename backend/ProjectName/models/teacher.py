from . import db


class Teacher(db.Model):
    __tablename__ = 'teacher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    cardNumber = db.Column(db.String(30))
