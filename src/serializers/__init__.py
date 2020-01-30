from marshmallow import Schema, fields, post_load

from src.models import BasicResponse, Ingredient


class IngredientSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    calories = fields.Float()

    @post_load
    def make_object(self, data, *args, **kwargs):
        return Ingredient(**data)


class BasicResponseSchema(Schema):
    result = fields.Raw()
    error = fields.Raw(allow_none=True)

    @post_load
    def make_object(self, data, *args, **kwargs):
        return BasicResponse(**data)
