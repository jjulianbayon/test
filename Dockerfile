# escape=`FROM --platform=$TARGETPLATFORM python:3.8-alpine
FROM python:3.8-alpine
WORKDIR /app

RUN pip3 install pytest

COPY . .

CMD [ "python3", "holamundo.py"]