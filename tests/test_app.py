import pytest
from tornado.web import Application

from src import make_app


def test_create_app():
    app = make_app()
    assert isinstance(app, Application)


@pytest.mark.gen_test
async def test_app_listen(http_client, base_url):
    response = await http_client.fetch(f"{base_url}")

    assert response.code == 200
