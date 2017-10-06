FROM python:3
RUN mkdir /webapp
WORKDIR /webapp
ADD requirements.txt /webapp/
RUN pip install -r requirements.txt
ADD . /webapp/