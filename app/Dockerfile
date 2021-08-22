FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock
COPY ./app /opt/app/app

RUN apt-get update -y
RUN  apt-get install dpkg curl chromium unzip -y
RUN apt-get clean -y
RUN rm -rf /var/lib/apt/lists/*

# TODO: このドライバはchromium-browserに依存しているが、インストールできない
RUN curl -L "http://launchpadlibrarian.net/533923221/chromium-chromedriver_90.0.4430.72-0ubuntu0.16.04.1_arm64.deb" \
    -o chromedriver_90.0.4430.72-0ubuntu0.16.04.1_arm64.deb
RUN dpkg -i chromedriver_90.0.4430.72-0ubuntu0.16.04.1_arm64.deb

RUN useradd -s /bin/bash -m myuser
USER myuser

ENV PATH /home/myuser/.local/bin:$PATH

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.lock \
 && rm -rf ~/.cache/pip/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--proxy-headers", "--forwarded-allow-ips", "*"]
