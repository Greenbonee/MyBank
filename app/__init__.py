from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import customer, manager, admin
    app.register_blueprint(customer.bp)
    app.register_blueprint(manager.bp)
    app.register_blueprint(admin.bp)

    return app