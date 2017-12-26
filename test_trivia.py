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

    def clear(self):
        self.strings = []


class TestRoll:

    number_by_category = {
        1: 'Science',
        2: 'Rock',
        3: 'Sports',
        4: 'Sports',
        5: 'Rock',
        6: 'Science',
    }

    def test_roll_for_science(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        for number, category in self.number_by_category.items():
            game.roll(number)
            assert f'The category is {category}' in print.strings
            print.clear()
