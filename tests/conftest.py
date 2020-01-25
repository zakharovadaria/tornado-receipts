import pytest

from src import make_app


@pytest.fixture
def app():
    app = make_app()
    return app
