# -*- coding: utf-8 -*-
from flask import Flask, Response, request
from yagls import batch, data_transfer, config

app = Flask(__name__)
app.register_blueprint(batch.batch_endpoint)
app.register_blueprint(data_transfer.data_transfer_endpoint)

if __name__ == "__main__":
    if config.DEBUG:
        app.run(debug=True)
    else:
        from gevent.wsgi import WSGIServer
        http_server = WSGI_Server(("", config.PORT), app)
        http_server.serve_forever()
