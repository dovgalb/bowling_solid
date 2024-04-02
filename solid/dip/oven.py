from abc import ABC, abstractmethod
from asyncio import wait

THERMOMETER = 0x86
FURNACE = 0x87
ENGAGE = 1
DISENGAGE = 0

# def regulate(min_temp, max_temp):
#     while True:
#         while read(THERMOMETER) > min_temp:
#             wait(1)
#         write(FURNACE, ENGAGE)
#         while read(THERMOMETER) < max_temp:
#             wait(1)
#         write(FURNACE, DISENGAGE)


class Thermometer(ABC):
    @abstractmethod
    def read(self):
        pass


class Heater(ABC):
    @abstractmethod
    def engage(self):
        pass

    @abstractmethod
    def disengage(self):
        pass


def regulate(t: Thermometer, h: Heater, min_temp, max_temp):
    while True:
        while t.read() > min_temp:
            wait(1)
        h.engage()
        while t.read() < max_temp:
            wait(1)
        h.disengage()