from tornado_sqlalchemy import SQLAlchemy


class Database:
    def __init__(self, url="postgresql://localhost:5432/tornado_receipts_development"):
        self.url = url
        self._db = None

    @property
    def instance(self):
        if not self._db:
            self._db = SQLAlchemy(self.url)

        return self._db

    def set_url(self, url):
        self.url = url
        self._db = SQLAlchemy(self.url)


db = Database()
