FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock
COPY ./app /opt/app/app

RUN apt-get update \
 && apt-get clean -y \
 && rm -rf /var/lib/apt/lists/* \
 && useradd -s /bin/bash -m myuser
USER myuser

ENV PATH /home/myuser/.local/bin:$PATH

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.lock \
 && rm -rf ~/.cache/pip/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--proxy-headers", "--forwarded-allow-ips", "*"]
