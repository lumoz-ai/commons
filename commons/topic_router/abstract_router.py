from abc import ABCMeta


class AbstractRouter(metaclass=ABCMeta):

    def __init__(self):
        pass

    @staticmethod
    def parse_topic(topic):
        # TODO refactor method to work for all scenarios
        split = topic.split("/")
        if topic.startswith("register"):
            topic_label = split[0]
            action = "register"
        else:
            topic_label = split[3]
            action = split[4]

        return topic_label, action
