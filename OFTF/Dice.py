import random

class Dice:

    def __init__(self):
        pass

    def roll(self, num_dice):
        outcome = list()
        for i in range(num_dice):
            outcome.append(random.randrange(1,7))

        return outcome