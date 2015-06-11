#!/bin/bash
node master.js &
sleep 2
node worker.js &
node worker.js &
node worker.js