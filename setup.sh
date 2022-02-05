#!/bin/bash
dir="$(pwd)"

cp -r ./src/flaskapp ./docker/api/
cp -r ./bots ./docker/api


docker compose build --pull