FROM python:3-alpine
MAINTAINER ox.peregud@gmail.com
RUN apk update && apk add python3
RUN pip3 install --no-cache-dir flask
ADD py_server.py /
CMD [ "python3", "./py_server.py" ]
EXPOSE 5000
