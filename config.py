class BaseConfig:
    USER_DB = 'postgres'
    PASS_DB = 'AZXW157e'
    URL_DB = 'localhost'
    NAME_DB ='manga_bd'
    FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SECRET_KEY = "secretKEY1232"
    SQLALCHEMY_DATABASE_URI = FULL_URL_DB
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False