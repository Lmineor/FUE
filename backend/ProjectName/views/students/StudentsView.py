from flask import request
from flask import Blueprint
from flask import jsonify
from sqlalchemy.sql.expression import func

from ...logger import logger
from ...models.students import Students
from ...models import db


students = Blueprint('students', __name__)


@students.route('/students', methods=['POST', 'GET'])
def get_students_info():
    """
    students 视图逻辑
    """
    if request.method == 'GET':
        pass
    else:
        pass
