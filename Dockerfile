FROM alpine

RUN apk --no-cache add python3 \
                       build-base \
                       python3-dev \
                       # wget dependency
                       openssl \
                       # dev dependencies
                       git \
                       bash \
                       sudo \
                       py3-pip


RUN mkdir /app

ADD app /app

WORKDIR /app

RUN pip3 install -r requirements.txt
