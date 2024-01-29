import unittest
from unittest.mock import patch
from game.utils import get_user_choice

class TestUtils(unittest.TestCase):

    @patch('builtins.input', side_effect=['rock'])
    def test_get_user_choice_rock(self, mock_input):
        self.assertEqual(get_user_choice(), 'rock')

    @patch('builtins.input', side_effect=['paper'])
    def test_get_user_choice_paper(self, mock_input):
        self.assertEqual(get_user_choice(), 'paper')

    @patch('builtins.input', side_effect=['scissors'])
    def test_get_user_choice_scissors(self, mock_input):
        self.assertEqual(get_user_choice(), 'scissors')

    @patch('builtins.input', side_effect=['invalid', 'rock'])
    def test_get_user_choice_invalid_then_rock(self, mock_input):
        self.assertEqual(get_user_choice(), 'rock')

if __name__ == '__main__':
    unittest.main()
