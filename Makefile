all: init exec

init:
	cp ./src/web/index.js ./web/public_html/assets/js/index.js
	docker compose build --pull

exec:
	docker compose up

.PHONY: init exec