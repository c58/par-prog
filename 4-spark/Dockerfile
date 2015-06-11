FROM sequenceiq/spark:1.3.0-ubuntu

# Prepare hadoop
RUN \
  apt-get update && \
  apt-get install -y build-essential python-pip python-dev git && \
  pip install hdfs

ENV PATH /usr/local/hadoop/bin:$PATH
ENV HADOOP_HOME /usr/local/hadoop-2.6.0/share/hadoop/tools/lib/

# Run our task
ADD ./ /app
WORKDIR /app
CMD ["sh", "startup.sh"]
