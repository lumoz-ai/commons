import json
from abc import ABCMeta

from commons.constants import EXACTLY_ONCE
from commons.mqtt.publisher import MQTTPublisher
from commons.schema import ResponseSchema, ResponseSchemaModel


class Action(metaclass=ABCMeta):

    def __init__(self):
        self.publisher = MQTTPublisher()
        self.action_map = None

    def execute(self, action, payload):
        action_method = self.action_map.get(action)
        payload = json.loads(payload)
        action_method(**payload)

    @staticmethod
    def validate_response(payload) -> ResponseSchemaModel:
        schema = ResponseSchema()
        response = schema.load(payload)
        if isinstance(response, ResponseSchemaModel):
            return response
        else:
            raise TypeError("response is not of type", ResponseSchemaModel)
