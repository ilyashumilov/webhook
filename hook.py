import logging
import os
import sys
from threading import Thread

import requests
from flask import Flask, request
from handler import handler

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_update():
    if request.method == "POST":
        data = request.json
        handler(data)
    return {"ok": True}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
