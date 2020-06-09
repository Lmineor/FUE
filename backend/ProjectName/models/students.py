from . import db


class Students(db.Model):
    __bind_key__ = 'students'  # 已设置__bind_key__ 数据库名
    __tablename__ = 'songshiauthor' # 表名

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    cardNumber = db.Column(db.String(30))
