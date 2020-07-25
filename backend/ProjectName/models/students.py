from . import db


class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    cardNumber = db.Column(db.String(30))
