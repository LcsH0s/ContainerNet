FROM python:3

COPY ./flaskapp /flaskapp

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN cd / && ls -al
RUN pip install -r /flaskapp/requirements.txt