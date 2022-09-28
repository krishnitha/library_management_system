from flask import request
from flask.views import MethodView
from lms.models.book_model import Book
from lms.serializer.book_serializer import book, books
from lms.resource.book_resource import get_all_book, add_book, get_book_info


class BookAddView(MethodView):

    @staticmethod
    def get():
        status = 200
        book_list = get_all_book()
        if len(book_list) == 0:
            status = 204
        return books.dump(book_list), status

    @staticmethod
    def post():
        name = request.json['name']
        publisher = request.json['publisher']
        author = request.json['author']
        new_book = Book(name=name, publisher=publisher, author=author)
        add_book(new_book)
        return book.dump(new_book), 201


class BookDetailView(MethodView):

    @staticmethod
    def get(book_id):
        status = 200
        book_info = get_book_info(book_id)
        if book_info is None:
            status = 204
        return book.dump(book_info), status

