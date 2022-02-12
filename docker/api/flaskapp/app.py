#!/usr/bin/env python
# encoding: utf-8

import flask
import json
from flask_cors import CORS

import botManager

app = flask.Flask(__name__)
CORS(app)
bot_manager = botManager.BotManager()


@app.route('/', methods=['GET'])
def def_root():
    try:
        bot_manager.add(context=f'/bots/test',
                        name='test',
                        token='OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.nBwsdDhEmfOoEKHJLGvdmXwsDxg'
                        )
        bot_manager.start('test')
    except ReferenceError:
        pass

    return "ddx manager api"


@app.route('/manage/add', methods=['POST'])
def api_add():
    request_data = flask.request.get_json()
    try:
        bot_manager.add(context=request_data['context'],
                        token=request_data['token'],
                        name=request_data['name']
                        )
        return 'OK'
    except Exception:
        return 'BAD ARGUMENTS'


@app.route('/manage/start', methods=['POST'])
def api_start():
    request_data = flask.request.get_json()
    try:
        bot_manager.start(request_data['name'])
        return 'OK'
    except Exception:
        return 'BAD NAME'


@app.route('/bots/online', methods=['GET'])
def get_online_bots():
    online = bot_manager.get_online_bots()
    if (online):
        return json.dumps(online, indent=4)
    return "No bots online!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, ssl_context=(
        '/flaskapp/certs/cert.pem', '/flaskapp/certs/key.pem'), debug=True)
