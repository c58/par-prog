FROM node:0.10.38

# Prepare environment
RUN \
  apt-get update && \
  apt-get install -y build-essential libzmq3-dev

# Prepare python
WORKDIR /app
RUN \
  npm install zmq && \
  npm install express

# Run our task
EXPOSE 8080
ADD ./ /app
CMD ["sh", "startup.sh"]
