from sqlalchemy import Column, Integer, String, Float

from src.db import db

target_metadata = db.instance.metadata


class Ingredient(db.instance.Model):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    calories = Column(Float)

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', calories={self.calories})"

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id


class BasicResponse:
    def __init__(self, result=None, error=None):
        self.result = result
        self.error = error
