from lms import db


class User(db.Model):
    username = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    library = db.relationship('Library', backref='user', lazy=True)

    def __init__(self, username, email, name):
        self.username = username
        self.email = email
        self.name = name
