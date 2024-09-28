FROM python:3.12
LABEL authors="Dmitry"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt update -y
RUN apt-get install gcc musl-dev bash zlib1g-dev libjpeg-dev -y && \
    apt-get autoremove -y && apt-get clean

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.3 POETRY_HOME=/root/poetry python3 -
ENV PATH="${PATH}:/root/poetry/bin"

COPY poetry.lock pyproject.toml /
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

WORKDIR /opt
COPY ./ /opt

EXPOSE 8000
