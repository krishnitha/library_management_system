from lms import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    library = db.relationship('Library', backref='book', lazy=True)

    def __init__(self, name, publisher, author):
        self.name = name
        self.publisher = publisher
        self.author = author
