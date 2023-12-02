class BowlingGame:
    def __init__(self):
        # Initialize a new bowling game
        self.rolls = []

    def roll(self, pins):
        # Record the roll of a bowling ball.
        self.rolls.append(pins)

    def score(self):
        # Calculate and return the total score of the game
        result = 0
        roll_index = 0

        for frame_index in range(10):
            if roll_index < len(self.rolls):

                if self.is_strike(roll_index):
                    result += self.strike_score(roll_index)
                    roll_index += 1
                elif self.is_spare(roll_index):
                    result += self.spare_score(roll_index)
                    roll_index += 2
                else:
                    result += self.frame_score(roll_index)
                    roll_index += 2

        return result

    def is_strike(self, roll_index):
        # Check if the roll at the given index is a strike
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        # Check if the consecutive rolls form a spare.
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_score(self, roll_index):
        # The function calculate the score for a strike frame.
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_score(self, roll_index):
        # Calculate the score for a spare frame.
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        # calculate the score for a normal frame.
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
