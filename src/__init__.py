from tornado.web import Application

from src.controllers import MainHandler


def make_app():
    return Application([
        (r"/", MainHandler),
    ])
