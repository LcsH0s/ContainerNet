#!/usr/bin/env python
# encoding: utf-8


import flask
import json
from flask_cors import CORS

import ddx

app = flask.Flask(__name__)
CORS(app)
bot_manager = ddx.manager.ContainerManager()


@app.route('/', methods=['GET'])
def def_root():
    try:
        bot_manager.add(context=f'/bots/test',
                        name='test',
                        token='OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.nBwsdDhEmfOoEKHJLGvdmXwsDxg'
                        )
        bot_manager.start('test')

    except ReferenceError as e:
        return str(e)
    except Exception as e:
        return f'Unhandeled error : {e}'

    if not (bot_manager.get_bot_by_name('test').is_running()):
        raise(bot_manager.Error(
            'Initialization Error : Something went wrong when initializing the bot'))

    return "Success"


@app.route('/discord/bots', methods=['POST'])
def api_add():
    request_data = flask.request.get_json()
    try:
        bot_manager.add(context=request_data['context'],
                        token=request_data['token'],
                        name=request_data['name']
                        )
        return 'OK'
    except Exception as e:
        return f'BAD ARGUMENTS : {e}'


@app.route('/discord/bots', methods=['PUT'])
def api_start():
    request_data = flask.request.get_json()
    try:
        if(request_data['action'] == 'start'):
            try:
                bot_manager.start(request_data['name'])
                return 'OK'
            except Exception as e:
                return f'BAD NAME : {e}'
        elif (request_data['action'] == 'stop'):
            try:
                bot_manager.stop(request_data['name'])
                return 'OK'
            except Exception as e:
                return f'BAD NAME : {e}'
    except Exception as e:
        return f'bad action : {e}'


@app.route('/discord/bots/online', methods=['GET'])
def get_online_bots():
    online = bot_manager.get_online_bots()
    if (online):
        return json.dumps(online, indent=4)
    return "No bots online!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, ssl_context=(
        '/flaskapp/certs/cert.pem', '/flaskapp/certs/key.pem'), debug=True)
