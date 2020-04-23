from singleton_decorator import singleton


@singleton
class MQTTSubscriber:

    def __init__(self):
        self.client = None
        self.router = None

    def setup_router(self, router):
        self.router = router

    def set_client(self, client):
        self.client = client

    def on_message(self, client, userdata, msg):
        print(msg)
        try:
            data = {
                "topic": msg.topic,
                "payload": msg.payload
            }
            topic = msg.topic
            payload = msg.payload
            self.router.route(topic, payload)
        except Exception as e:
            print(e)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)
