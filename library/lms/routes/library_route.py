from flask import Blueprint

from lms.views import library_view

library_route = Blueprint('library', __name__)

library_route.add_url_rule('/library/books/', 'book_list',
                           library_view.LibraryBookAddView.as_view('book_list'),
                           methods=['GET'])

library_route.add_url_rule('/library/books/<int:book_id>/', 'book_detail',
                           library_view.LibraryBookDetailView.as_view('book_detail'),
                           methods=['GET'])

library_route.add_url_rule('/library/books/', 'add_book',
                           library_view.LibraryBookAddView.as_view('add_book'),
                           methods=['POST'])

library_route.add_url_rule('/library/users/', 'user_list',
                           library_view.LibraryUserListView.as_view('user_list'),
                           methods=['GET'])

library_route.add_url_rule('/library/users/<string:username>/', 'user_detail',
                           library_view.LibraryUserDetailView.as_view('user_detail'),
                           methods=['GET'])

library_route.add_url_rule('/library/users/', 'add_user',
                           library_view.LibraryAddUserView.as_view('add_user'),
                           methods=['POST'])

library_route.add_url_rule('/library/users/<string:username>/books/<int:book_id>/', 'issue_detail',
                           library_view.LibraryIssueView.as_view('issue_detail'),
                           methods=['POST'])