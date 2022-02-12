#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_cors import CORS
from botManager.botManager import botManager

WORKDIR = ""

app = Flask(__name__)
CORS(app)
manager = botManager()


@app.route('/', methods=['GET'])
def def_root():
    manager.add('test', '/bots/music_test/', 'awdawdawdawdawdawdawdawda')
    manager.start('test')
    return "ddx manager api"


@app.route('/bots/online', methods=['GET'])
def get_online_bots():
    return 'test'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, ssl_context=(
        '/flaskapp/certs/cert.pem', '/flaskapp/certs/key.pem'), debug=True)
