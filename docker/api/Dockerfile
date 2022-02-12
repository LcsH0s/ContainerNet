FROM python:3

COPY ./docker/api/flaskapp/requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY ./docker/api/flaskapp /flaskapp
COPY ./bots /bots
CMD /usr/local/bin/python /flaskapp/app.py