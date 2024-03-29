import pytest


class Frame:
    def __init__(self):
        self._score = 0
    @property
    def score(self):
        return self._score

    def add(self, pins):
        self._score += pins


class FrameTest:
    def test_score_no_throws(self):
        f = Frame()
        assert f.score == 0

    def test_add_one_throw(self):
        f = Frame()
        f.add(5)
        assert f.score == 5
