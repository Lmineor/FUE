### local_config.py 配置示例

```py
DB_User = "root" # 默认的用户名
DB_Psw = "123456" # 密码
Default_DB = {
        "username": DB_User,
        "password": DB_Psw,
        "db": "ii"
    }

# 需要绑定的多个数据库
# 可以指定不同的数据库名称，用户名，密码
BINDS_DB = [{
        "username": DB_User,
        "password": DB_Psw,
        "db": "xx"
    }, {
        "username": DB_User,
        "password": DB_Psw,
        "db": "zz"
    }, {
        "username": DB_User,
        "password": DB_Psw,
        "db": "yy"
    }
]

SECRET_KEY = 'xxxxxxxxxxx'  # 生成Token时自己指定的密钥，相当于随机种子吧

DEV = True  # Flask的debug模式开关

# 电子邮件配置模块
MAIL_HOST = "smtp.163.com"          # 设置服务器
MAIL_USER = "example@163.com"    # 用户名,一般指你的邮箱名称
MAIL_PASS = "xxxx"            # 口令 

Domain = "127.0.0.1:5000"           # API
FrontDomain = "127.0.0.1:3000"      # 网站的域名
```