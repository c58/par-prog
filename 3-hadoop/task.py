# -*- coding: utf-8
import hadoopy
import os
import logging


input_path = '/data/corpus_data'
output_path = '/data/output'
local_path = '/app/opencorpora'

# Utilities
def read_local_dir(local_path):
  for fn in os.listdir(local_path):
    path = os.path.join(local_path, fn)
    if os.path.isfile(path):
      yield path, open(path).read()

# Cleanup and write input data
if hadoopy.exists(input_path):
  hadoopy.rmr(input_path)
if hadoopy.exists(output_path):
  hadoopy.rmr(output_path)
hadoopy.writetb(input_path, read_local_dir(local_path))

# Launch the job
hadoopy.launch_frozen(input_path, output_path, 'wc.py')

# Read the first KV pair
word_counts = dict(hadoopy.readtb(output_path))
for w3, tpl in word_counts.items():
  if tpl[1] > 4:
    print tpl[0][0], tpl[0][1], tpl[0][2], tpl[1], tpl[2], tpl[3]