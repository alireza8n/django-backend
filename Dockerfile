FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set common work directory
WORKDIR /opt/app

# Install required dependencies
RUN apt-get update
RUN apt-get install -y --fix-missing --no-install-recommends gcc libpq-dev procps vim netcat gettext

# Configure Timezone
ENV TIME_ZONE=Asia/Tehran
RUN echo 'Configuring timezone:' $TIME_ZONE \
    && ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime \
    && echo $TIME_ZONE > /etc/timezonero

# Copy pip installed packages
COPY requirements.txt .
RUN pip install --disable-pip-version-check -r requirements.txt

# Mount sourse code
COPY src src
WORKDIR /opt/app/src

ENTRYPOINT ["bash", "docker-entrypoint.sh"]

EXPOSE 8000
