import pika
import uuid


class PdfRpcClient(object):

    def __init__(self):

        self.credentials = pika.PlainCredentials('root', 'root')
        self.parameters =  pika.ConnectionParameters('rabbitmq', credentials=self.credentials, heartbeat=5)
        self.connection = pika.BlockingConnection(self.parameters)
        # self.connection = pika.BlockingConnection(
        #     pika.ConnectionParameters(host='rabbitmq'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, data):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=data)
        while self.response is None:
            self.connection.process_data_events()
        return self.response