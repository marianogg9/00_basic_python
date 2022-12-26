#!/usr/bin/env python
# encoding: utf-8
import json
from os import abort
from urllib import request

from flask import Flask
app = Flask(__name__)

tokens = {
    "jean.dupont": "120wdosdfoi3"
}


def get_token(credentials: dict):

    username = credentials["username"]
    password = credentials["password"]

    if username == "jean.dupont" and password == "123":
        return tokens[username]
    else:
        abort(403)


@app.route('/tokens', methods=["GET", "POST"])
def tokens():
    content = request.get_json()
    token = get_token(content)

    return {
        "token": token
    }


app.run()
