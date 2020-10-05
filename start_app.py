from gevent.pywsgi import WSGIServer
from fib_challenge import app

def run_server():
    try:
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
    except Exception as e:
        return ("There was an issue running the server:{}".format(str(e)))

if __name__ == "__main__":
    run_server()
