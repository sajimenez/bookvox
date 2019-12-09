FROM python:3.7-alpine
LABEL Sebastian Jimenez

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . .

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN apk add libxml2-dev libxslt-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN adduser -D user
USER user