from datetime import datetime


def before():
    print("start time: ", datetime.now().time())


def after(req):
    print("end time: ", datetime.now().time())
    return req


def init_middlewares(app):
    app.before_request(before)
    app.after_request(after)
