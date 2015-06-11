#!/usr/bin/env python
import sys, glob
sys.path.append('gen-py')

import logging
from ranker import Ranker
from ranker.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from urlparse import urlparse
from pyquery import PyQuery as pq
from lxml import etree
import urllib

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logging.getLogger("thrift.server.TServer").addHandler(ch)

class RankerHandler:
  def getNodesByUrl(self, url):
    nodes = set()

    try:
      d = pq(url=url, opener=lambda url, **kw: urllib.urlopen(url).read())
      tmp = d("[href],[src]")
      for i in range(0, len(tmp)):
        link = pq(tmp[i]).attr("href")
        if not link:
          link = pq(n).attr("src")
        node = urlparse(link).hostname
        if node:
          nodes.add(node)
    except Exception, e:
      pass

    return list(nodes)

handler = RankerHandler()
processor = Ranker.Processor(handler)
transport = TSocket.TServerSocket(port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.serve()