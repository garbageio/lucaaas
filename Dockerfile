FROM python:3.7.2-stretch
RUN apt-get update -y
RUN pip install redisai numpy flask flask-cors ml2rt
RUN git clone https://github.com/chrisPiemonte/eaas.git
ENV FLASK_APP=app.py
WORKDIR /eaas
EXPOSE 5000
ENTRYPOINT [ "flask" ]
CMD [ "run", "-h", "0.0.0.0", "--port", "5000"]
