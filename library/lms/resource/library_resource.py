from lms.database import db
from lms.models.library_model import Library


def get_user_book(username):
    return Library.query.filter_by(username=username)


def add_user_book(book_issue):
    db.session.add(book_issue)
    db.session.commit()