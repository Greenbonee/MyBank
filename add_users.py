from app import create_app, db
from app.models import User, Role
from flask_security.utils import hash_password
import uuid

app = create_app()

with app.app_context():
    # Add roles if they do not exist
    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    
    manager_role = Role.query.filter_by(name='manager').first()
    if not manager_role:
        manager_role = Role(name='manager')
        db.session.add(manager_role)
    
    # Add admin user if it does not exist
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        admin_user = User(
            username='admin',
            email='admin@gmail.com',
            password_hash=hash_password('adminpassword'),
            active=True,
            fs_uniquifier=str(uuid.uuid4())
        )
        admin_user.roles.append(admin_role)
        db.session.add(admin_user)
    
    # Add manager user if it does not exist
    manager_user = User.query.filter_by(username='manager').first()
    if not manager_user:
        manager_user = User(
            username='manager',
            email='manager@gmail.com',
            password_hash=hash_password('managerpassword'),
            active=True,
            fs_uniquifier=str(uuid.uuid4())
        )
        manager_user.roles.append(manager_role)
        db.session.add(manager_user)
    
    db.session.commit()
    print("Admin and Manager users added successfully!")
