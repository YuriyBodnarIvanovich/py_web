import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 5050
    MAIL_USERNAME = '22usyk08@gmail.com'
    MAIL_PASSWORD = '***'
    MAIL_USE_TLS = False
    MAILS_USE_SSL = True
