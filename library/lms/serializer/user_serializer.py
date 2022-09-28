
from lms import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email', 'name')


user = UserSchema()
users = UserSchema(many=True)