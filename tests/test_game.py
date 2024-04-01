import pytest
from model.game import Game


class TestGame:
    @pytest.fixture
    def game(self):
        return Game()

    def test_one_throw(self, game):
        game.add(5)
        assert game.score == 5

    def test_two_throws_no_mark(self, game):
        game.add(5)
        game.add(4)
        assert game.score == 9
        assert game.current_frame == 2

    def test_four_throw_no_mark(self, game):
        # game: Game = Game()
        game.add(5)
        game.add(4)
        game.add(7)
        game.add(2)
        assert game.score == 18
        assert game.score_for_frame(1) == 9
        assert game.score_for_frame(2) == 18
        assert game.current_frame == 3

    def test_simple_spare(self, game):
        game.add(3)
        game.add(7)
        game.add(3)
        assert game.score_for_frame(1) == 13

    def test_simple_frame_after_spare(self, game):
        game.add(3)
        game.add(7)
        game.add(3)
        game.add(2)
        assert game.score_for_frame(1) == 13
        assert game.score_for_frame(2) == 18
