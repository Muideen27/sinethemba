from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure the app here
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Leye:leye@localhost/my_love'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:leye@localhost/love'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from views import views
    app.register_blueprint(views, url_prefix='/')

    return app
