FROM python:3

COPY ./docker/api/flaskapp /flaskapp
COPY ./docker/api/bots /bots

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /flaskapp/requirements.txt

CMD /usr/local/bin/python /flaskapp/app.py