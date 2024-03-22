from settings import settings
from client import channel
from validators import number_validator


def _base_sender(routing_key: str, value: str, prefix):
    if value := number_validator(value):
        body = f'{prefix}-{value}'
        sent = channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=bytes(body, 'utf-8')
        )
        print(f'----SUCCESSFULLY SENT {routing_key} -- {value}')
        return sent
    raise TypeError('value must be int or float type')


def send_first_number():
    send_body = input('Input number 1: ')

    return _base_sender(
        settings.QUEUE_NAME,
        value=send_body,
        prefix=settings.NUMBER_KEY_1
    )


def send_second_number():
    send_body = input('Input number 2: ')

    return _base_sender(
        settings.QUEUE_NAME,
        value=send_body,
        prefix=settings.NUMBER_KEY_2
    )


if __name__ == '__main__':
    send_first_number()
    send_second_number()
