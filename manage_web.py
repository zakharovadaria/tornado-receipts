from tornado.ioloop import IOLoop

from src import make_app

if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"App listen on port {port}")
    IOLoop.current().start()
