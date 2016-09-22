# -*- coding: utf-8 -*-
from __future__ import print_function

import ConfigParser
import json
from sys import stderr
from os import path, makedirs

from flask import Flask, Response, request
from yagls import batch, data_transfer

app = Flask(__name__)
app.register_blueprint(batch.batch_endpoint)
app.register_blueprint(data_transfer.data_transfer_endpoint)

if __name__ == "__main__":
    app.run(debug=True)
