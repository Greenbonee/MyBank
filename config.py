import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'super-secret-salt'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
