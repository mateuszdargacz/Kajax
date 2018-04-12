FROM alpine

RUN apk --no-cache add build-base \
                       python3-dev \
                       bash \
                       py3-pip \
                       jpeg-dev \
                       zlib-dev


RUN mkdir /app

ADD app /app

WORKDIR /app

RUN pip3 install -r requirements.txt
