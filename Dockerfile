FROM python:3.7.2-stretch
RUN apt-get update -y
# RUN pip install redisai numpy flask flask-cors ml2rt
# RUN git clone https://github.com/chrisPiemonte/eaas.git
ADD . /eaas/
WORKDIR /eaas
RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT [ "flask" ]
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
# CMD [ "run", "-h", "0.0.0.0", "--port", "5000"]
