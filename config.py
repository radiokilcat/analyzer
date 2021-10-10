import os
import pathlib


class Config():
    DEBUG = True

    ### Upload settings
    UPLOAD_FOLDER = os.path.abspath(os.getenv('FILES_DIR',
                                              f'{pathlib.Path()}/files/'))



    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

    ### DataBase Configuration ###
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              f'sqlite:///{pathlib.Path().absolute()}/app.db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_USER = {'username':'admin', 'password': '123456'}

    ### Admin Configuration ###
    SECRET_KEY = 'i do not know how to use it right' #TODO: Do it right

