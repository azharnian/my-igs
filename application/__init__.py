from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_redis import FlaskRedis
from flask_cors import CORS

from application.project.settings import Settings

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
redis = FlaskRedis()
cors = CORS()

def create_app(config_class=Settings):
    app = Flask(__name__, template_folder='views')
    app.config.from_object(Settings)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    redis.init_app(app)
    cors.init_app(app)

    from application.project.routes import projects
    from application.users.routes import users
    from application.achievements.routes import achievements
    from application.certificates.routes import certificates

    app.register_blueprint(projects)
    app.register_blueprint(users)
    app.register_blueprint(achievements)
    app.register_blueprint(certificates)

    return app

