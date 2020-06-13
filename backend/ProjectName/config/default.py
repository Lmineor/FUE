# encoding:utf-8
# default.py

r"""FUE default config file
Comlete your own config here
"""
import os

__doc__ = r"""You can import local_config to this file"""



try:
    from .local_config import *
except ImportError:
    pass


class DefaultConfig(object):

    # Default Database URI
    SQLALCHEMY_DATABASE_URI = 'mysql://{username}:{password}@localhost:3306/{db}'.format(**Default_DB)

    # 需要绑定的多个数据库
    SQLALCHEMY_BINDS = {'{db}'.format(**item):'mysql://{username}:{password}@localhost:3306/{db}'.format(**item) for item in BINDS_DB}

    # Secret Key for Token
    SECRET_KEY = SECRET_KEY

    # Cache(for file cache)
    FILESYSTEM = {
		'CACHE_TYPE': 'filesystem',
		'CACHE_DIR': './flask_cache',
		'CACHE_DEFAULT_TIMEOUT': 922337203685477580,
		'CACHE_THRESHOLD': 922337203685477580
	}
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    SESSION_TIME = 30*60  # session 有效期
    
    EXPIRATION = 60*60*1  # auth有效期1小时
    
    LOGPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

