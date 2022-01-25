#!/bin/bash
dir="$(pwd)"

cp -r ./src/flaskapp ./docker/api/

docker compose build --pull