from lms.models.book_model import Book
from lms.database import db


def get_all_book():
    return Book.query.all()


def add_book(new_book):
    db.session.add(new_book)
    db.session.commit()


def get_book_info(book_id):
    return Book.query.filter_by(id=book_id).first()

