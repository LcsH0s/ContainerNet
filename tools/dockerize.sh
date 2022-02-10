#! /bin/bash

# This script takes as arguemnts : the path to the bot repo, the name of the bot
# It create a Dockerfile located in the /tmp/dockerfiles/<name specified in arguement> and copies all of the bot files

if [ "$#" -ne 1 ]
then 
    echo "Illegal number of parameters: Please specify the path to the bot repo and the name of the bot (the repo name and bot name has to be the same)"
    exit
fi

NAME=$2
F_PATH=./tmp/dockerfiles/$NAME
LOCAL=$(pwd)
DCKRF=./tmp/dockerfiles/$NAME/Dockerfile

cd ..
cp -r $1 ./tmp/dockerfiles
echo "FROM python:latest" > $DCKRF 
echo "ADD ./app / " >> $DCKRF 
echo "ADD ./requirements.txt / " >> $DCKRF 
echo "RUN pip install -r /requirements.txt" >> $DCKRF 
echo "CMD python /app/main.py" >> $DCKRF

cd $LOCAL
