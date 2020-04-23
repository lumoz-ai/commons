from marshmallow import Schema, fields, post_load


class TopicSchema(Schema):
    topic_id = fields.Str(data_key="topicId", required=True)
    task = fields.Str(data_key="task", required=True)
    topic = fields.Str(data_key="topic", required=True)
    is_subscribe = fields.Int(data_key="isSubscribe", required=True)
    is_publish = fields.Int(data_key="isPublish", required=True)

    @post_load
    def make_topic(self, data, **kwargs):
        return TopicSchemaModel(**data)


class TopicSchemaModel:
    def __init__(self, topic_id, task, topic, is_subscribe, is_publish):
        self.topic_id = topic_id
        self.task = task
        self.topic = topic
        self.is_subscribe = is_subscribe
        self.is_publish = is_publish
