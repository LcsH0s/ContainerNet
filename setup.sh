cp -r ./src/flaskapp ./docker/api/
cp ./src/web/index.js ./docker/web/public_html/assets/js/index.js

docker compose build --pull