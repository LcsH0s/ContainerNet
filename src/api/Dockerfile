FROM python:3

COPY ./src/api/flaskapp/requirements.txt /requirements.txt
COPY ./src/ddx/ /ddx

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install /ddx
RUN pip install -r /requirements.txt

COPY ./src/api/flaskapp /flaskapp
COPY ./bots /bots
CMD /usr/local/bin/python /flaskapp/app.py