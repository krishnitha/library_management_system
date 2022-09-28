from flask import Blueprint

from lms.views import user_view

user_route = Blueprint('user', __name__)


user_route.add_url_rule('/users/', 'user_list',
                        user_view.UserAddView.as_view('user_list'),
                        methods=['GET'])

user_route.add_url_rule('/users/<string:username>/', 'user_detail',
                        user_view.UserDetailView.as_view('user_detail'),
                        methods=['GET'])

user_route.add_url_rule('/users/', 'add_user',
                        user_view.UserAddView.as_view('add_user'),
                        methods=['POST'])