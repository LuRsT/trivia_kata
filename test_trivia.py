import builtins

from trivia import Game



class MockPrint:
    """
    This is to patch print and check what's happening

    """
    def __init__(self):
        self.strings = []

    def __call__(self, value):
        self.strings.append(value)


class TestTrivia:

    def test_roll_for_science(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(1)
        assert 'The category is Science' in print.strings

    def test_roll_for_sports(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(2)
        assert 'The category is Sports' in print.strings

    def test_roll_for_rock(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(3)
        assert 'The category is Rock' in print.strings

    def test_roll_for_pop(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(4)
        assert 'The category is Pop' in print.strings

    def test_roll_for_science(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(5)
        assert 'The category is Science' in print.strings

    def test_roll_for_sports_2(self):
        # wat?!
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        game.roll(6)
        assert 'The category is Sports' in print.strings
