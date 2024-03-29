class Frame:
    def __init__(self):
        self._score = 0
        self._throws = [0] * 21
        self._current_throw = 0

    @property
    def score(self):
        return self._score

    def add(self, pins):
        self._throws[self._current_throw] = pins
        self._current_throw += 1
        self._score += pins

    def score_for_frame(self, frame: int):
        score: int = 0
        ball: int = 0
        for current_frame in range(frame):
            score += self._throws[ball] + self._throws[ball+1]
            ball += 2
        return score
