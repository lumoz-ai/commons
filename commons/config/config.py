from abc import ABCMeta, abstractmethod


class Config(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def get(self):
        pass
