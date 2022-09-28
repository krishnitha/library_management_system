
from lms import ma


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'publisher', 'author')


book = BookSchema()
books = BookSchema(many=True)