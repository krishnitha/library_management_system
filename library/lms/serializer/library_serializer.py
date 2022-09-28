
from lms import ma


class LibrarySchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'book_id')


class UserBookSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email', 'name', 'books')


library = LibrarySchema()
library_schema = LibrarySchema(many=True)
user_book_schema = UserBookSchema()