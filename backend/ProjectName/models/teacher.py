from . import db


class Teacher(db.Model):
    __bind_key__ = 'teacher'  # 已设置__bind_key__ 数据库名
    __tablename__ = 'tablename2' # 表名

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    cardNumber = db.Column(db.String(30))
