from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin

from src.models import Ingredient, BasicResponse
from src.serializers import IngredientSchema, BasicResponseSchema


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world!")


class IngredientsHandler(SessionMixin, RequestHandler):
    def get(self):
        with self.make_session() as session:
            ingredients = session.query(Ingredient).all()
            ingredients = IngredientSchema().dump(ingredients, many=True)

            response = BasicResponse(result=ingredients, error=None)
            self.write(BasicResponseSchema().dump(response))
