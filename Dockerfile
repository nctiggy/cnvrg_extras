FROM python:3-alpine

LABEL maintainer="craig.smith@cnvrg.io"

RUN apk add --no-cache --virtual .build-deps \
            openssh \
            build-base \
            libffi-dev \
            openssl-dev && \
    apk add --no-cache git && \
    pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir cnvrgv2>=1.0.9 && \
    apk del .build-deps
