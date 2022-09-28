from flask import Blueprint

from lms.views import book_view

book_route = Blueprint('book', __name__)

book_route.add_url_rule('/books/', 'book_list',
                        book_view.BookAddView.as_view('book_list'),
                        methods=['GET'])

book_route.add_url_rule('/books/<int:book_id>/', 'book_detail',
                        book_view.BookDetailView.as_view('book_detail'),
                        methods=['GET'])

book_route.add_url_rule('/books/', 'add_book',
                        book_view.BookAddView.as_view('add_book'),
                        methods=['POST'])