class Config:
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/CamBear_DB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False