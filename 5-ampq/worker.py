# -*- coding: utf-8
import pika
from subprocess import Popen, PIPE, STDOUT

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def mystem(str_to_analyse):
  p = Popen(['mystem', '-gnid'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
  grep_stdout = p.communicate(input=str_to_analyse)[0]
  return grep_stdout

def on_request(ch, method, props, body):
    n = body

    print " [.] mystem(%s)"  % (n,)
    response = mystem(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print " [x] Awaiting RPC requests"
channel.start_consuming()