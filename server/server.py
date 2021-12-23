import pika
import create_pdf as create_pdf

credentials = pika.PlainCredentials('root', 'root')
parameters =  pika.ConnectionParameters('rabbitmq', credentials=credentials, heartbeat=5)
connection = pika.BlockingConnection(parameters)

# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='rabbitmq'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def pdf(data):
    res = create_pdf.create(data)
    return res

def on_request(ch, method, props, body):
    data = body
    response = pdf(data)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()