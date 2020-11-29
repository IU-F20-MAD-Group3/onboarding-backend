ARG PYTHON_VERSION="3.8"

FROM python:$PYTHON_VERSION

RUN set -ex; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
      netcat; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /

RUN pip install --no-cache -r /requirements.txt

COPY src/ .

COPY docker/docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE "8000"

VOLUME ["/data"]

CMD ["uwsgi"]
