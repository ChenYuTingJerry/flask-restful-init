from kombu import Connection
from kombu.pools import producers

__all__ = ['producer']


class _Producer:
    def __init__(self):
        self._connection = None

    def init(self, app):
        self._connection = Connection(app.config['BROKER_URL'])

    def publish(self, body, exchange='', routing_key='', delivery_mode=2, serializer='json', retry=False):
        with producers[self._connection].acquire(block=True) as prod:
            prod.publish(body, exchange=exchange, routing_key=routing_key, delivery_mode=delivery_mode,
                         serializer=serializer, retry=retry)


producer = _Producer()
