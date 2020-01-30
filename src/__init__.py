from tornado.web import Application

from src.controllers import MainHandler, IngredientsHandler
from src.db import db


def make_app():
    return Application([
        (r"/", MainHandler),
        (r"/ingredients", IngredientsHandler)
    ], db=db.instance)
