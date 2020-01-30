from tornado.web import Application

from src.controllers import MainHandler
from src.db import db


def make_app():
    return Application([
        (r"/", MainHandler),
    ], db=db.instance)
