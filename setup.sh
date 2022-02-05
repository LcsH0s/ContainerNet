#!/bin/bash
dir="$(pwd)"

cp -r ./src/flaskapp ./docker/api/
cp -r ./bots ./docker/api
cp ./src/web/index.js ./docker/web/public_html/assets/js

docker compose build --pull