import pytest
from sqlalchemy_utils import database_exists, create_database, drop_database
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

from src import make_app
from src.models import Ingredient
from src.db import db

url = "postgresql://localhost:5432/tornado_receipts_test"


def migrate_db(database_url: str):
    alembic_config = AlembicConfig("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", database_url)
    alembic_upgrade(alembic_config, "head")


def truncate_db(session):
    session.query(Ingredient).delete()


@pytest.fixture
def app():
    app = make_app()
    return app


@pytest.fixture(scope="session", autouse=True)
def init_db():
    if database_exists(url):
        drop_database(url)

    create_database(url)
    migrate_db(url)
    db.set_url(url)

    yield

    drop_database(url)


@pytest.fixture
def database():
    return db.instance


@pytest.fixture
def session(database):
    session = database.sessionmaker(bind=database.engine)
    truncate_db(session)
    yield session
    session.close()
