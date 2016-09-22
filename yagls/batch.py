# -*- coding: utf-8 -*-
from __future__ import print_function
from os import path,makedirs
import json

from flask import Blueprint, Response, request

batch_endpoint = Blueprint("batch_endpoint", __name__)


@batch_endpoint.route("/<path:repo>/objects/batch", methods=["POST"])
def batch(repo):
    hacc = request.headers.get("Accept")
    hcty = request.headers.get("Content-Type")
    if ("application/vnd.git-lfs+json" not in hacc
            or "application/vnd.git-lfs+json" not in hcty):
        return Response("Bad request: missing headers", 400)

    req = json.loads(request.data)
    out_status = 200

    if req["operation"] == "upload":
        out = {"objects": __upload(repo, req["objects"])}
    elif req["operation"] == "download":
        out = {"objects": __download(repo, req["objects"])}
    else:
        out = {"message": "Invalid operation"}
        out_status = 500

    resp = Response(json.dumps(out), out_status)
    resp.headers["Content-Type"] = "application/vnd.git-lfs+json"
    return resp


def __upload(repo, req_data):
    """ TODO: Validation """
    if not path.exists(repo):
        makedirs(repo)

    ret = []
    for obj in req_data:
        obj["actions"] = {"upload": {
            "href": "http://localhost:5000/{0}/upload/{1}".format(
                repo, obj["oid"]
            )
        }}
        ret.append(obj)

    return ret


def __download(repo, req_data):
    norepo = False
    if not path.exists(repo):
        norepo = True
    
    ret = []
    for obj in req_data:
        if (path.isfile("{0}/{1}".format(repo_path, obj["oid"]))
                and not norepo):
            obj["actions"] = {"download": {
                "href": "http://localhost:5000/{0}/{1}".format(
                    repo, obj["oid"]
                )
            }}
        else:
            obj["error"] = {
                "code": 404,
                "message": "Object does not exist"
            }
        ret.append(obj)

    return ret
