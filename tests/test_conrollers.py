import pytest
from tornado.escape import json_decode

from src.models import Ingredient
from src.serializers import BasicResponseSchema, IngredientSchema


@pytest.mark.gen_test
async def test_base_get(http_client, base_url):
    response = await http_client.fetch(base_url)

    assert response.body == b"Hello, world!"


@pytest.mark.gen_test
async def test_get_ingredients_status_code(http_client, base_url, session):
    response = await http_client.fetch(f"{base_url}/ingredients")

    assert response.code == 200

    ingredient = Ingredient(name="Test", calories=200)
    session.add(ingredient)
    session.commit()

    response = await http_client.fetch(f"{base_url}/ingredients")
    body = json_decode(response.body)
    basic_response = BasicResponseSchema().load(body)

    actual = IngredientSchema().load(basic_response.result[0])
    assert actual == ingredient
