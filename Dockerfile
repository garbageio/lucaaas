#  FROM python:3.7.2-stretch
#  RUN apt-get update -y
#  RUN apt-get install -y apache2-dev
# RUN pip install redisai numpy flask flask-cors ml2rt
# RUN git clone https://github.com/chrisPiemonte/eaas.git
#  ADD . /eaas/
#  WORKDIR /eaas
#  RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT [ "flask" ]
#  CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
# CMD [ "run", "-h", "0.0.0.0", "--port", "5000"]


#Grab the latest alpine image
# FROM alpine:latest

FROM python:3.7-stretch
RUN apt-get update -y
RUN apt-get install -y apache2-dev

# Install python and pip
# RUN apk add --no-cache --update python3 py3-pip bash
ADD . /eaas/
WORKDIR /eaas

# Install dependencies
RUN pip3 install --no-cache-dir -q -r requirements.txt

RUN adduser -D myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
