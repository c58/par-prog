FROM rabbitmq

# Prepare environment
RUN \
  apt-get update && \
  apt-get install -y build-essential python-pip python-dev git wget

# Install mystem
RUN \
  mkdir /tmp/mystem && cd /tmp/mystem && \
  wget http://download.cdn.yandex.net/mystem/mystem-3.0-linux3.1-64bit.tar.gz && \
  tar -xzvf *.tar.gz && cp mystem /usr/local/bin && \
  chmod +x /usr/local/bin/mystem

# Prepare python
RUN \
  pip install pika

# Run our task
ADD ./ /app
WORKDIR /app
CMD ["sh", "startup.sh"]
