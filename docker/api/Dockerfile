FROM python:3

COPY ./docker/api/flaskapp /flaskapp
WORKDIR /flaskapp

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN cd / && ls -al
RUN pip install -r ./requirements.txt

CMD /usr/local/bin/python app.py