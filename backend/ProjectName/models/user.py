from werkzeug.security import generate_password_hash, check_password_hash # 转换密码用到的库
from flask_security import UserMixin # 登录和角色需要继承的对象
from itsdangerous import TimedJSONWebSignatureSerializer as SignatureExpired, BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from ..config.default import DefaultConfig
from ..models import db


class User(db.Model, UserMixin):
    __bind_key__ = 'user'
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    memo = db.Column(db.Text)

    def __repr__(self):
        return "<User_id:{0}>".format(self.id)

    @property
    def password(self):
        raise AttributeError("密码不允许读取")

    # 转换密码为hash存入数据库
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 检查密码
    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)

    # 获取token，有效时间1天
    def generate_auth_token(self, expiration=DefaultConfig.EXPIRATION):
        s = Serializer(DefaultConfig.SECRET_KEY, expires_in=expiration)
        return s.dumps({'id': self.id})

    # 解析token，确认登录的用户身份
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(DefaultConfig.SECRET_KEY)
        try:
            data = s.loads(token)
        except BadSignature as e:
            return None  # invalid token
        except Exception as e:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user
