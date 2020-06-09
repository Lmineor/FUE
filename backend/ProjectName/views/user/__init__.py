from flask import Blueprint
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

user = Blueprint('user', __name__)
