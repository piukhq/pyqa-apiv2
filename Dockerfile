FROM ghcr.io/binkhq/python:3.11
ARG PIP_INDEX_URL
ARG APP_NAME
ARG APP_VERSION
RUN pip install --no-cache ${APP_NAME}==$(echo ${APP_VERSION} | cut -c 2-)
RUN apt-get update \
    && apt-get -y --no-install-recommends install curl \
    && curl -sL https://aka.ms/InstallAzureCLIDeb | bash \
    && apt-get autoremove -y curl \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
ADD . .
