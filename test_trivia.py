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


class TestAdd:

    def test_add_one_player(self):
        game = Game()
        player_name = 'Chet'

        builtins.print = MockPrint()
        game.add(player_name)
        assert f'{player_name} was added' in print.strings
        assert 'They are player number 1' in print.strings


class TestRoll:

    categories = [
        'Science',
        'Rock',
        'Sports',
        'Sports',
        'Rock',
        'Science',
        'Pop',
    ]

    def test_roll_for_science(self):
        game = Game()
        game.add('Chet')

        builtins.print = MockPrint()
        for number, category in enumerate(self.categories, start=1):
            game.roll(number)
            assert f'The category is {category}' in print.strings
            print.clear()
