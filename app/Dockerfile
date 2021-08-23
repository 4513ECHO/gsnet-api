FROM python:3.9-slim-buster

WORKDIR /opt/app

COPY ./requirements.lock /tmp/requirements.lock
COPY ./app /opt/app/app

RUN apt-get update -y \
 && apt-get install -y dpkg wget unzip software-properties-common gnupg
RUN add-apt-repository ppa:canonical-chromium-builds/stage -y
RUN cat <<EOF | sudo tee /etc/apt/preferences.d/pin-xalt7x-chromium-deb-vaapi \
Package: * \
Pin: release o=LP-PPA-xalt7x-chromium-deb-vaapi \
Pin-Priority: 1337 \ 
EOF
RUN apt-get update -y
RUN apt-get install chromium-browser -y
RUN apt-get clean -y \
 && rm -rf /var/lib/apt/lists/*

RUN wget http://launchpadlibrarian.net/533923221/chromium-chromedriver_90.0.4430.72-0ubuntu0.16.04.1_arm64.deb
RUN dpkg -i chromium-chromedriver_90.0.4430.72-0ubuntu0.16.04.1_arm64.deb

RUN useradd -s /bin/bash -m myuser
USER myuser

ENV PATH /home/myuser/.local/bin:$PATH

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.lock \
 && rm -rf ~/.cache/pip/*

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--proxy-headers", "--forwarded-allow-ips", "*"]
