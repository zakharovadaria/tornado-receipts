from src.models import Ingredient


def test_str_ingredient():
    ingredient = Ingredient(name="test", calories=200)

    assert str(ingredient) == "test"


def test_repr_ingredient():
    ingredient = Ingredient(name="test", calories=200)

    assert repr(ingredient) == "Ingredient(name='test', calories=200)"


def test_create_ingredient(session):
    ingredient = Ingredient(name="test", calories=200)

    session.add(ingredient)
    session.commit()

    saved_ingredient = session.query(Ingredient).first()

    assert ingredient == saved_ingredient
