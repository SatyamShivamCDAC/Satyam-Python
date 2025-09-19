from abc import ABC, abstractmethod


class DesertItem(ABC):

    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_cost(self):
        pass

    def get_name(self):
        return self.price

    def __str__(self):
        return "Desert : " + self.name