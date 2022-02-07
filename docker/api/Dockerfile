FROM python:3

COPY ./docker/api/flaskapp/requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /requirements.txt

ENV TEST_TOKEN 'OTM5OTc0NzE4MDk2ODE4MTc2.YgAprA.k2qt8S6UPH_snFEfGnxbS60TeVQ'

COPY ./docker/api/flaskapp /flaskapp
COPY ./bots /bots
CMD /usr/local/bin/python /flaskapp/app.py