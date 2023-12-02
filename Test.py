


import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        
        # This function set up the environment for each test
        self.game = BowlingGame.BowlingGame()

    def test_gutter_game(self):
        # Test a scenario where no pins are knocked down in any roll of the game
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score () == 0
        
    def test_all_ones(self):
        
        self.rollMany(1, 20)
        assert self.game.score () == 20
        
    def test_one_spare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score () == 16
        
    def test_one_strike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score () == 24
        
    def test_perfect_game(self):
        self.rollMany(10,12)
        assert self.game.score () == 300
        
    def test_one_spare(self):
        self.rollMany(5,21)
        assert self.game.score () == 150
        
    def roll_many(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
			


