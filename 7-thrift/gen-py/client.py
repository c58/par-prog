#!/usr/bin/env python
import sys, glob
sys.path.append('gen-py')

from ranker import Ranker
from ranker.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from collections import Counter

try:
  transport = TSocket.TSocket('localhost' , 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = Ranker.Client(protocol)
  transport.open()

  nodes = Counter()
  with open('./links.txt') as f:
    lines = f.read().splitlines()
    for url in lines:
      enil = Counter(client.getNodesByUrl(url))
      nodes = nodes + enil

  sortedNodes = sorted(nodes.items(), key=lambda x: -x[1])[:10]
  for (node, count) in sortedNodes:
    print node, count

  transport.close ()
except Thrift.TException, tx:
  print '%s' % (tx.message)