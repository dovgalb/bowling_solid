class Game:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    def add(self, pins):
        self._score += pins

    def score_for_frame(self, frame: int):
        return 0