FROM python:3.9-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock
COPY ./app /opt/app/app

RUN wget https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+files/chromium-codecs-ffmpeg_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && wget https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+files/chromium-codecs-ffmpeg-extra_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && wget https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+files/chromium-browser_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && wget https://launchpad.net/~canonical-chromium-builds/+archive/ubuntu/stage/+files/chromium-chromedriver_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && apt update \
 && apt install -y ./chromium-codecs-ffmpeg_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && apt install -y ./chromium-codecs-ffmpeg-extra_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && apt install -y ./chromium-browser_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && apt install -y ./chromium-chromedriver_90.0.4430.93-0ubuntu0.16.04.1_arm64.deb \
 && apt clean \ 
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
