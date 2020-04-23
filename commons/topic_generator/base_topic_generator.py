class BaseTopicGenerator:

    def __init__(self, source, destination):
        self.base = ""
        self.source = source
        self.destination = destination
        self.published_by_source = []
        self.subscribed_by_source = []

    def get_topics_published_by_source(self):
        topics = self._get_topics(self.source, self.destination, self.published_by_source)
        return topics

    def get_topics_subscribed_by_source(self):
        topics = self._get_topics(self.destination, self.source, self.subscribed_by_source)
        return topics

    def _get_topics(self, source, destination, tasks):
        topics = []
        for task in tasks:
            topic = task, self._generate_topic(source, destination, task)
            topics.append(topic)
        return topics

    def _generate_topic(self, source, destination, task):
        return "{}/{}/{}/{}".format(source, destination, self.base, task)
