from settings import settings
from client import channel
from num_counter import num_counter


def callback(ch, method, properties, body):
    number_key, value = str(body, 'utf-8').split('-')
    value = float(value)
    setattr(num_counter, number_key, value)
    num_counter()


channel.basic_consume(
    on_message_callback=callback,
    queue=settings.QUEUE_NAME,
    auto_ack=True
)

print(f'STARTING CONSUMER...')
channel.start_consuming()
