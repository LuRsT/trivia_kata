from trivia import Game


class TestTrivia:

    def test_it(self):
        game = Game()
        game.add('Chet')
        assert len(game.players) == 2
