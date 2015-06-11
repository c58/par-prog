#!/bin/bash
/etc/bootstrap.sh
hdfs dfsadmin -safemode leave
python task.py