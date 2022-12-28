# pull official base image
FROM python:3.11-alpine
# set work directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add tk-dev

RUN apk update \
    $$ apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app/innotter/
# install dependencies
COPY Pipfile* /usr/src/app/
RUN pip install pipenv && pipenv install --deploy --system --ignore-pipfile

# copy project
COPY . .

ENTRYPOINT ["/usr/src/app/innotter/entrypoint.sh"]