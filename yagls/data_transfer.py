# -*- coding: utf-8 -*-
from __future__ import print_function
from os import path,makedirs
import gc

import json
from flask import Blueprint, Response, request

data_transfer_endpoint = Blueprint("data_transfer_endpoint", __name__)


@data_transfer_endpoint.route("/<path:repo>/upload/<oid>", methods=['PUT'])
def object_upload(repo, oid):
    response_code = 200
    response_message = "Upload successful"
    try:
        if path.exists(repo):
            with open("{0}/{1}".format(repo, oid), "w") as file: 
                file.write(request.data)
        else:
            response_code = 404
            response_message = "Repository {0} does not exist".format(repo)
    except IOError as e:
        response_code = 500
        response_message = "I/O Error: ({0}) {1}".format(e.errno, e.strerror)

    resp = Response(json.dumps({"message":response_message}), response_code)
    resp.headers["Content-Type"] = "application/vnd.git-lfs+json"
    return resp


@data_transfer_endpoint.route("/<path:object_path>", methods=['GET'])
def object_download(object_path):
#    if path.isfile(object_path):
#        pass
#        
    resp = Response('{"message": "Well sh1t"}', 501)
    resp.headers["Content-Type"] = "application/vnd.git-lfs+json"
    return resp
