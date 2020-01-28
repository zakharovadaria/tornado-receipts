import os

from tornado.ioloop import IOLoop

from src import make_app

app = make_app()

if __name__ == "__main__":
    port = os.environ.get("PORT")
    app.listen(port)
    print(f"App listen on port {port}")
    IOLoop.current().start()
