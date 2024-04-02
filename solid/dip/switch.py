from abc import ABC


class Switchable(ABC):
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(Switchable):
    def turn_on(self):
        print('Свет включен...')

    def turn_off(self):
        print('Свет выключен...')

class Spotlight(Switchable):
    def turn_on(self):
        print('Прожектор включен...')

    def turn_off(self):
        print('Прожектор выключен...')


class Switch:
    def __init__(self, switchable: Switchable):
        self.switchable = switchable

    def flip(self):
        self.switchable.turn_on()
        self.switchable.turn_off()



light = Light()
spotlight = Spotlight()

Switch(light).flip()

