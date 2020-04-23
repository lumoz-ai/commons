from commons.mqtt.client import MQTTClient


class Bootstrap:

    def __init__(self, message_broker, port, component_list, topic_routes=None):
        self.message_broker = message_broker
        self.port = port
        self.component_list = component_list
        self.topic_routes = topic_routes
        self.mqtt_client = MQTTClient()
        self.mqtt_client.setup_router(topic_routes)

    def boot(self):
        self.mqtt_client.register_callbacks(on_connect=self.on_connect)
        self.connect()

    def connect(self):
        self.mqtt_client.connect(self.message_broker, self.port)

    def on_connect(self, client, userdata, flags, rc):
        print("connected")
        for component in self.component_list:
            # component_instance = component()
            component.start()
