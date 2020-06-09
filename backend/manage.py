from flask_script import Manager

from ProjectName import create_app
from ProjectName.models import db

app = create_app()
manager = Manager(app)



@manager.command
def schema_create():
    db.create_all()
    print('you had create all tables')


@manager.command
def schema_drop():
    db.drop_all()
    print('you had drop all tables')


@manager.command
def schema_update():
    db.create_all()
    print('you had update all tables')


@manager.command
def list_routes():
    for rule in app.url_map.iter_rules():
        print(rule)


if __name__ == '__main__':
    manager.run()