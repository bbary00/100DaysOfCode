from game import get_random_number, Game
from unittest.mock import patch
import pytest
import mock
import random
from redditimagescraper import RedditImageScraper

@patch.object(random, 'randint')
def test_get_random_number(m):
    m.return_value = 20
    assert get_random_number() == 20


# @patch("builtins.input", lambda x: [11, '12', 'bob', 12, 5, -1, 21, 7, None])
# def test_input():
#     game = Game()
#     # good
#     assert game.check_number() == 11
#     assert game.check_number() == 12
#     # Nan
#     with pytest.raises(ValueError):
#         game.check_number()
#     # 12 guessed
#     with pytest.raises(ValueError):
#         game.check_number()
#     # good
#     assert game.check_number() == 5
#     # out of range
#     with pytest.raises(ValueError):
#         game.check_number()
#     with pytest.raises(ValueError):
#         game.check_number()
#     # good
#     assert game.check_number() == 7
#     # hit enter
#     with pytest.raises(ValueError):
#         game.check_number()


f1 = lambda x: x
f2 = lambda x: str(x)
@pytest.mark.parametrize('valid_values', [f(i) for i in range(1, 101) for f in
                                          (f1, f2)])
def test_what_year(valid_values):
    game = Game()
    # years = a bunch of invalid inputs with a valid input at the end
    invalid = [None, "9999", "0", "", " ", "-2015", "-30", str(10^1000),
               'bob', valid_values]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=invalid):
        assert RedditImageScraper.game.check_number('start') == int(valid_values)