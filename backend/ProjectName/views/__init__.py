from ..views.students import StudentsView
from ..views.user import UserView


def register_blueprints(app):
    app.register_blueprint(StudentsView.poem, url_prefix='/students')
    app.register_blueprint(UserView.user, url_prefix='/user')