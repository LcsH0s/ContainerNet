FROM python:3

COPY ./src/api/flaskapp/requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN python3 -m pip install -r /requirements.txt

COPY ./src/api/flaskapp /flaskapp
COPY ./src/ddxl /flaskapp/ddxl
COPY ./bots /bots

CMD python3 /flaskapp/app.py