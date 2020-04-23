from abc import ABCMeta, abstractmethod
from commons.constants import EXACTLY_ONCE, ALMOST_ONCE, ATLEAST_ONCE
from commons.mqtt import MQTTPublisher, MQTTSubscriber


class Component(metaclass=ABCMeta):

    def __init__(self):
        self.mqtt_publisher = MQTTPublisher()
        self.mqtt_subscriber = MQTTSubscriber()

    @abstractmethod
    def start(self):
        pass

    @staticmethod
    def validate_qos(qos):
        valid_qos = [EXACTLY_ONCE, ATLEAST_ONCE, ALMOST_ONCE]
        if qos not in valid_qos:
            raise ValueError("QOS must be one of ", ",".join(valid_qos))

    @staticmethod
    def make_mqtt_response(status, response_to, data=None):
        result = dict(status=status, data=data, responseTo=response_to)
        return result

    def publish_message(self, topic, payload, qos=EXACTLY_ONCE):
        self.validate_qos(qos)
        self.mqtt_publisher.publish(topic, payload, qos)
