import logging
import os
import sys
from threading import Thread

import requests
from flask import Flask, request
# from main import handler

app = Flask(__name__)


@app.route("/", methods=["POST"])
def receive_update():
    if request.method == "POST":
        # print('sdfbskdbkjfbk')
    # logging.info(request.get_json())
    # print('asldknflaskjgdkjbkj')
        print(request.form)
    # msg = {
    #     "id": request.get_json()["message"]["chat"]["id"],
    #     "from": request.get_json()["message"]["chat"]["first_name"],
    #     "text": request.get_json()["message"]["text"],
    # }
    # print(msg, flush=True)
    # thread = Thread(target=handler, args=(msg,))
    # thread.start()


    return {"ok": True}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
