from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def toWalk(self):
        pass

    def hello(self):
        print("hello world")

class Cat(Animal):
    def toWalk(self):
        print("Cat walks")

cat = Cat()
cat.toWalk()
cat.hello()