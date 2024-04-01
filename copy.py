class Copier:
    @staticmethod
    def copy():
        c = Keyboard.read()
        while c != -1:
            Printer.write(c)
            c = Keyboard.read()


class Copier:
    ptFlag = False

    @staticmethod
    def copy():
        c = 0
        while True:
            if Copier.ptFlag:
                c = PaperTape.read()
            else:
                c = Keyboard.read()

            if c == -1:
                break

            Printer.write(c)


class Copier:
    ptFlag = False
    punchFlag = False

    @staticmethod
    def copy():
        c = 0
        while True:
            if Copier.ptFlag:
                c = PaperTape.read()
            else:
                c = Keyboard.read()

            if c == -1:
                break

            if Copier.punchFlag:
                PaperTape.punch(c)
            else:
                Printer.write(c)
###################################################################


class Reader:
    def read(self):
        pass


class KeyboardReader(Reader):
    def read(self):
        return Keyboard.read()


class Copier:
    reader = KeyboardReader()

    @staticmethod
    def copy():
        c = 0
        while True:
            c = Copier.reader.read()
            if c == -1:
                break
            Printer.write(c)