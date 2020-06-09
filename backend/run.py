from ProjectName import create_app
from ProjectName.config.local_config import DEV

app = create_app()

if __name__ == '__main__':
    app.run(debug=DEV)
