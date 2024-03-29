import pytest
from model.game import Game


class TestGame:
    def test_one_throw(self):
        game = Game()
        game.add(5)
        assert game.score == 5

    def test_two_throws_no_mark(self):
        game = Game()
        game.add(5)
        game.add(4)
        assert game.score == 9

    def test_four_throw_no_mark(self):
        game: Game = Game()
        game.add(5)
        game.add(4)
        game.add(7)
        game.add(2)
        assert game.score == 18
        assert game.score_for_frame(1) == 9
        assert game.score_for_frame(2) == 18
