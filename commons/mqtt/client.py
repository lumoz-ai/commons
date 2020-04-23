from paho.mqtt.client import Client
from singleton_decorator import singleton

from commons.mqtt.publisher import MQTTPublisher
from commons.mqtt.subscriber import MQTTSubscriber


@singleton
class MQTTClient:

    def __init__(self):
        self.client = Client()
        self.subscriber = MQTTSubscriber()
        self.publisher = MQTTPublisher()
        self.subscriber.set_client(self.client)
        self.publisher.set_client(self.client)
        self.topic_router = None

    def setup_router(self, router):
        self.topic_router = router
        self.subscriber.router = router

    def connect(self, broker_ip, port):
        self.client.connect(broker_ip, port, 60)
        self.client.loop_forever()

    def register_callbacks(self, on_connect=None):
        self.client.on_connect = on_connect
        self.client.on_message = self.subscriber.on_message

    def on_connect(self):
        pass
