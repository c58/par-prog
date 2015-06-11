FROM ubuntu:latest

# Prepare environment
RUN \
  apt-get update && \
  apt-get install -y build-essential python-pip python-dev git wget

# Install Thrift
ENV THRIFT_VERSION 0.9.2
RUN buildDeps=" \
    automake \
    bison \
    curl \
    flex \
    g++ \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-test-dev \
    libevent-dev \
    libssl-dev \
    libtool \
    make \
    pkg-config \
  "; \
  apt-get update && apt-get install -y --no-install-recommends $buildDeps && rm -rf /var/lib/apt/lists/* \
  && curl -sSL "http://apache.mirrors.spacedump.net/thrift/$THRIFT_VERSION/thrift-$THRIFT_VERSION.tar.gz" -o thrift.tar.gz \
  && mkdir -p /usr/src/thrift \
  && tar zxf thrift.tar.gz -C /usr/src/thrift --strip-components=1 \
  && rm thrift.tar.gz \
  && cd /usr/src/thrift \
  && ./configure  --without-cpp \
  && make \
  && make install \
  && cd / \
  && rm -rf /usr/src/thrift \
  && apt-get purge -y --auto-remove $buildDeps

# Prepare python
RUN \
  apt-get update && apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev && \
  pip install thrift && \
  pip install pyquery

# Run our task
ADD ./ /app
WORKDIR /app
CMD ["sh", "startup.sh"]
