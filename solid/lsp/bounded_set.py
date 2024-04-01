from abc import ABC, abstractmethod

class Set(ABC):
    @abstractmethod
    def add(self, o):
        pass

    @abstractmethod
    def delete(self, o):
        pass

    @abstractmethod
    def is_member(self, o):
        pass


def print_set(s: Set):
    for o in s:
        print(o)