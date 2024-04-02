from abc import ABC, abstractmethod


class TimerClient(ABC):
    @abstractmethod
    def timeout(self):
        pass


class Door(TimerClient):
    def lock(self):
        pass

    def unlock(self):
        pass

    def is_door_open(self):
        pass

    def timeout(self):
        pass



class Timer:
    def register(self, timeout: int, client: "TimerClient"):
        client.timeout()


