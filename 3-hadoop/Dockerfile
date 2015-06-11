FROM sequenceiq/hadoop-ubuntu:2.6.0

# Prepare environment
RUN \
  apt-get update && \
  apt-get install -y build-essential python-pip python-dev git && \
  pip install -e git+https://github.com/bwhite/hadoopy#egg=hadoopy && \
  pip install pyinstaller

ENV PATH $PATH:/usr/local/hadoop/bin
ENV HADOOP_HOME /usr/local/hadoop-2.6.0/share/hadoop/tools/lib/

# Run our task
ADD ./ /app
WORKDIR /app
CMD ["sh", "startup.sh"]
