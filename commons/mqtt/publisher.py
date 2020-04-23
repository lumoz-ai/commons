from singleton_decorator import singleton
from commons.constants import EXACTLY_ONCE
import json

from commons.utils import PayloadEncoder


@singleton
class MQTTPublisher:
    _instance = None

    def __init__(self):
        self.client = None

    def set_client(self, client):
        self.client = client

    def publish(self, topic, payload, qos=EXACTLY_ONCE):
        try:
            payload = json.dumps(payload, cls=PayloadEncoder)
            self.client.publish(topic, payload, qos)
        except Exception as e:
            print(e)
