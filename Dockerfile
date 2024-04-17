FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY src/mosamaticweb .
COPY requirements.txt .
COPY docker-entrypoint.sh .

RUN apt-get update \
    && apt-get install -y vim curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["/usr/src/app/docker-entrypoint.sh"]