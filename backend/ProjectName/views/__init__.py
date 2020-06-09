from ..views.user import UserView
from ..views.teacher import TeacherView
from ..views.students import StudentsView


def register_blueprints(app):
    app.register_blueprint(UserView.user, url_prefix='/user')
    app.register_blueprint(StudentsView.students, url_prefix='/students')  # 之前定义的蓝图名称
    app.register_blueprint(TeacherView.teacher, url_prefix='/teacher')  # 之前定义的蓝图名称
