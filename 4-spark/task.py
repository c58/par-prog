# -*- coding: utf-8
import hdfs
import os
import logging
import sys
import math
from collections import Counter
from pyspark import SparkContext


input_path = '/data/corpus'
sc = SparkContext(appName = "TF-IDF")
files = sc.wholeTextFiles(input_path)
N = float(files.count())

words = files.map(lambda x: (x[0], x[1].split())) \
             .flatMap(lambda x: ((w, Counter({x[0]: 1})) for w in x[1])) \
             .reduceByKey(lambda a, b: a + b) \
             .flatMap(lambda x: ((fname, [(x[0], (count * math.log(N / len(x[1]))))]) for fname, count in x[1].items())) \
             .reduceByKey(lambda a, b: a + b)

output = words.collect()
for (doc, words) in output:
  sortedWords = sorted(words, key=lambda x: x[1])[-10:]
  print doc.encode("utf8")
  for (word, tfidf) in sortedWords:
    print "\t", word.encode("utf8"), tfidf

sc.stop()

