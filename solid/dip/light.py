from abc import ABC, abstractmethod


class LightInterface(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Lamp(LightInterface):
    def turn_on(self):
        print('лампа включена')

    def turn_off(self):
        print('лампа выключена')


class Button:
    def __init__(self, lamp: LightInterface):
        self.lamp = lamp
        self.condition = None

    def poll(self, condition: bool):
        if condition is True:
            self.lamp.turn_on()
            self.condition = True
        if condition is False:
            self.lamp.turn_off()


lamp = Lamp()
button = Button(lamp)
button.poll(True)
button.poll(False)