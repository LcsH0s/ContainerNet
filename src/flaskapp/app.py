#!/usr/bin/env python
# encoding: utf-8

import json
import os
from requests import request
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])

def query_records():
    return "yes"


@app.route('/', methods=['POST'])

def addBotToken():
    return "yes"
    

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5050)

