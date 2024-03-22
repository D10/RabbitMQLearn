import pika

from settings import settings

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=settings.QUEUE_NAME)
