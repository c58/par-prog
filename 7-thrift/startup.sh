#!/bin/bash
thrift -gen py ranker.thrift
python ./gen-py/server.py &
sleep 2
python ./gen-py/client.py