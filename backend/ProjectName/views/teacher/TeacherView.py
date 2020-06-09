from flask import request
from flask import Blueprint
from flask import jsonify
from sqlalchemy.sql.expression import func

from ...logger import logger
from ...models.teacher import Teacher
from ...models import db


teacher = Blueprint('teacher', __name__) # 蓝图名称


@students.route('/teacher', methods=['POST', 'GET'])
def get_teacher_info():
    """
    teacher 视图逻辑
    """
    if request.method == 'GET':
        pass
    else:
        pass
