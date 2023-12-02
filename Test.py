


import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        
        # This function set up the environment for each test
        self.game = BowlingGame.BowlingGame()
   
    def test_gutter_game(self):
        # Test a scenario where no pins are knocked down in any roll of the game
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score () == 0
        
    breakpoint()
    def test_all_ones(self):
        # test a game where all roll knock down one pin.
        self.roll_many(1, 20)
        assert self.game.score () == 20
        
    def test_one_spare(self):
        # Test a game with a spare in the first frame
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many (0,17)
        assert self.game.score () == 16
        
    def test_one_strike(self):
        # Test a game with a strike in the first frame.
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.roll_many(0,16)
        assert  self.game.score () == 24
        
    def test_perfect_game(self):
        # Test a perfect game with strikes in all frames.
        self.roll_many(10,12)
        assert self.game.score () == 300
        
    def test_one_spare(self):
        # Test a game with one spare in all frames.
        self.roll_many(5,21)
        assert self.game.score () == 150
        
    def roll_many(self, pins,rolls):
        # Roll the ball multiple times with the same number of pins knocked down.
        for i in range(rolls):
            self.game.roll(pins)
			

if __name__ == '__main__':
    unittest.main()

