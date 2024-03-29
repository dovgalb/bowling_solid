import pytest

from model.frame import Frame


class TestFrame:
    def test_score_no_throws(self):
        f = Frame()
        assert f.score == 0

    def test_add_one_throw(self):
        f = Frame()
        f.add(5)
        assert f.score == 5
