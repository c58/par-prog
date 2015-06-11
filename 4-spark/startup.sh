#!/bin/bash
/etc/bootstrap.sh
hdfs dfsadmin -safemode leave
hadoop fs -rmdir --ignore-fail-on-non-empty /data/corpus
hadoop fs -mkdir -p /data/corpus
hadoop fs -put /app/opencorpora/* /data/corpus
spark-submit task.py