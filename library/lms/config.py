
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    BASE_URL = "http://127.0.0.1:5000"
    SWAGGER_URL = '/lms'
    API_URL = '/static/swagger.json'

