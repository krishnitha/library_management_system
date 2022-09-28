from lms.models.user_model import User
from lms.database import db


def get_all_user():
    return User.query.all()


def add_user(new_user):
    db.session.add(new_user)
    db.session.commit()


def get_user_info(username):
    return User.query.filter_by(username=username).first()

