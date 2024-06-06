from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object('config.Config')

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models after db has been initialized
    from app.models import User, Role

    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    
    # Ensure database is created and roles are initialized within the app context
    with app.app_context():
        db.create_all()
        # Create roles if they don't exist
        if not Role.query.filter_by(name='admin').first():
            user_datastore.create_role(name='admin')
        if not Role.query.filter_by(name='manager').first():
            user_datastore.create_role(name='manager')
        if not Role.query.filter_by(name='customer').first():
            user_datastore.create_role(name='customer')
        db.session.commit()

    # Register blueprints after everything is initialized
    from app.web import views
    app.register_blueprint(views.bp)

    return app