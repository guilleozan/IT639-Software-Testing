
class BowlingGame:
    def __init__(self):
        # Initialize a new bowling game
        self.rolls=[]

    def roll(self,pins):
        self.rolls.append(pins)

    def score(self):
        # Calculate and return the total score of the game
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if frameIndex in range(10):
                result += self.StrikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
            rollIndex +=2
            return result

    def is_strike(self, rollIndex):
        # Check if the roll at the given index is a strike
        return self.rolls[rollIndex] == 10
    
    def is_spare(self, rollIndex):
        # Check if the consecutive rolls form a spare.
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    def sticke_score(self,rollIndex):
        # The function calculate the score for a strike frame.
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]
    

    def spare_score(self,rollIndex):
        # Calculate the score for a spare frame.
        return  10+ self.rolls[rollIndex+2]

    def frame_score(self, rollIndex):
        # calculate the score for a normal frame.
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		