import unittest
from game.mechanics import determine_winner

class TestGameMechanics(unittest.TestCase):
    
    def test_determine_winner(self):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
        self.assertEqual(determine_winner("paper", "rock"), "You win!")
        self.assertEqual(determine_winner("scissors", "paper"), "You win!")
        self.assertEqual(determine_winner("rock", "paper"), "Computer wins!")
        # Add more tests for different scenarios

if __name__ == '__main__':
    unittest.main()
