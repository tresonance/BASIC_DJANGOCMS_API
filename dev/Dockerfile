FROM python:3.7-alpine

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required package
RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    git bash

WORKDIR /app

COPY ./requirements.txt ./

# Install requirements.txt
RUN pip install -r ./requirements.txt

COPY .  .

# run entrypoint.sh
# ENTRYPOINT ["/app/entrypoint.sh"]

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000" ]