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
    login_manager.login_view = 'projects.index'
    login_manager.login_message_category = 'info'
    redis.init_app(app)
    cors.init_app(app)

    from application.project.routes import projects
    from application.admins.routes import admins
    from application.apis.routes import api
    from application.users.routes import users
    from application.achievements.routes import achievements
    from application.certificates.routes import certificates
    from application.attendances.routes import attendances
    from application.grades.routes import grades

    app.register_blueprint(projects)
    app.register_blueprint(admins, url_prefix = '/admin')
    app.register_blueprint(api, url_prefix = '/api')
    app.register_blueprint(users)
    app.register_blueprint(achievements, url_prefix = '/achievement')
    app.register_blueprint(certificates, url_prefix = '/certificate')
    app.register_blueprint(attendances, url_prefix = '/attendance')
    app.register_blueprint(grades, url_prefix = '/grade')

    return app

