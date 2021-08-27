FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock
COPY ./app /opt/app/app

RUN apt-get update -y
RUN apt-get install wget -y
RUN apt-get install chromium -y
RUN wget http://launchpadlibrarian.net/554114601/chromium-browser_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
RUN dpkg -i http://launchpadlibrarian.net/554114602/chromium-chromedriver_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
RUN wget http://launchpadlibrarian.net/554114602/chromium-chromedriver_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
RUN dpkg -i http://launchpadlibrarian.net/554114602/chromium-chromedriver_92.0.4515.159-0ubuntu0.18.04.1_arm64.deb
RUN apt-get clean -y \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -s /bin/bash -m myuser
USER myuser

ENV PATH /home/myuser/.local/bin:$PATH

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.lock \
 && rm -rf ~/.cache/pip/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--proxy-headers", "--forwarded-allow-ips", "*"]
