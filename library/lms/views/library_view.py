from flask import redirect, url_for, request, abort
from flask.views import MethodView
from lms.models.library_model import Library
from lms.serializer.user_serializer import user
from lms.serializer.book_serializer import book
from lms.serializer.library_serializer import library, library_schema, user_book_schema
from lms.resource.library_resource import get_user_book, add_user_book
from lms.resource.user_resource import get_user_info
from lms.resource.book_resource import get_book_info


class LibraryBookAddView(MethodView):

    @staticmethod
    def get():
        return redirect(url_for('book.book_list'))

    @staticmethod
    def post():
        return redirect(url_for('book.add_book', json=request.json), code=307)


class LibraryBookDetailView(MethodView):

    @staticmethod
    def get(book_id):
        return redirect(url_for('book.book_detail', book_id=book_id))


class LibraryUserListView(MethodView):

    @staticmethod
    def get():
        return redirect(url_for('user.user_list'))


class LibraryUserDetailView(MethodView):

    @staticmethod
    def get(username):
        book_list = get_user_book(username)
        user_books = library_schema.dump(book_list)
        if len(user_books) == 0:
            abort(400, "user as no book in library")
        else:
            user_info = get_user_info(username)
            user_detail = user.dump(user_info)
            book_detail = []
            for user_book in user_books:
                book_info = get_book_info(user_book['book_id'])
                book_detail.append(book.dump(book_info))
            return user_book_schema.dump(
                {
                    'username': user_detail['username'],
                    'email': user_detail['email'],
                    'name': user_detail['name'],
                    'books': book_detail
                }
            ), 200


class LibraryAddUserView(MethodView):

    @staticmethod
    def post():
        return redirect(url_for('user.add_user', json=request.json), code=307)


class LibraryIssueView(MethodView):

    @staticmethod
    def post(username, book_id):
        user_info = get_user_info(username)
        book_info = get_book_info(book_id)
        if user_info is None or book_info is None:
            abort(400, "User or Book is not available")
        else:
            book_issue = Library(username=username, book_id=book_id)
            add_user_book(book_issue)
            return library.dump(book_issue), 201
