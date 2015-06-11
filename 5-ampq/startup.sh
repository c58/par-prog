#!/bin/bash
rabbitmq-server > /dev/null 2>&1 &
sleep 5
python worker.py &
python client.py ./opencorpora/0003.txt