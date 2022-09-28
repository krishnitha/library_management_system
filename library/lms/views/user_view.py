from flask import request
from flask.views import MethodView
from lms.models.user_model import User
from lms.serializer.user_serializer import user, users
from lms.resource.user_resource import get_all_user, add_user, get_user_info


class UserAddView(MethodView):

    @staticmethod
    def get():
        status = 200
        user_list = get_all_user()
        if len(user_list) == 0:
            status = 204
        return users.dump(user_list), status

    @staticmethod
    def post():
        username = request.json['username']
        email = request.json['email']
        name = request.json['name']
        status = 400
        new_user = User(username=username, email=email, name=name)
        if get_user_info(username) is None:
            add_user(new_user)
            status = 201
        return user.dump(new_user), status


class UserDetailView(MethodView):

    @staticmethod
    def get(username):
        status = 200
        user_info = get_user_info(username)
        if user_info is None:
            status = 204
        return user.dump(user_info), status
