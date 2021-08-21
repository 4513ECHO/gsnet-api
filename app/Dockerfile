FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.lock\
 && apt-get update \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \

COPY ./app /opt/app/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--proxy-headers", "--forwarded-allow-ips", "*"]
