# -*- coding: utf-8
import pika
import uuid
import sys


class MystemRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, str_to_analyse):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(str_to_analyse))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

mystem_rpc = MystemRpcClient()

print " [x] Requesting mystem(...)"
response = mystem_rpc.call(open(sys.argv[1]).read())
print " [.] Got ", response