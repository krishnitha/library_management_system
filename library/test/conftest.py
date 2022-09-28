import pytest
from lms import create_app
from lms.models.library_model import Library
from lms.models.user_model import User
from lms.models.book_model import Book
from lms.serializer.book_serializer import book, books
from lms.serializer.library_serializer import library
from lms.serializer.user_serializer import user, users


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def sample_user():
    return User('raj', 'raj@gmail.com', 'raj')


@pytest.fixture
def sample_book():
    return Book('python', 'raj', 'raj')


@pytest.fixture
def sample_library():
    return Library('raj', 1)


@pytest.fixture()
def result_user(sample_user):
    return user.dump(sample_user)


@pytest.fixture()
def result_user_list(sample_user):
    return users.dump([sample_user])


@pytest.fixture()
def result_book(sample_book):
    return book.dump(sample_book)


@pytest.fixture()
def result_book_list(sample_book):
    return books.dump([sample_book])


@pytest.fixture()
def result_library(sample_library):
    return library.dump(sample_library)

