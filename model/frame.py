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

    def score_for_frame(self, the_frame: int):
        ball = 0
        score = 0
        current_frame = 0

        while current_frame < the_frame:
            first_throw = self._throws[ball]
            ball += 1
            second_throw = self._throws[ball]
            ball += 1
            frame_score = first_throw + second_throw

            if frame_score == 10:
                score += frame_score + self._throws[ball]
                ball += 1
            else:
                score += frame_score

            current_frame += 1
        return score
