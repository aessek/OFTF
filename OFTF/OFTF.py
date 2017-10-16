from Dice import Dice

class OFTF:

    def __init__(self):
        self.dice = Dice()
        self.score = 0
        self.saved_dice = []
        self.thrown_dice = []
        self.qualified = False
        self.results = 0

    def save_dice(self, dice):
        '''
        Adds the dice to your saved stack and removes it from the current throw
        '''
        for di in dice:
            self.saved_dice.append(di)
            self.thrown_dice.remove(di)

        return self
        
    def pick_highest(self, multiple=False):
        '''
        Finds the highest dice and selects it from the list of available dice. 
        If multiple is set to True, then if there are multiple of the determined
        highest dice, then it will grab all of them. E.g., it will grab three 6's
        instead of just one.
        '''
        picked_dice = []
        biggest = self.thrown_dice[0]

        if len(self.thrown_dice) is not 1:
            for i in range(len(self.thrown_dice)-1):
                next_dice = self.thrown_dice[i+1]
                if(next_dice > biggest):
                    biggest = next_dice

        if multiple is True:
            for _ in range(self.thrown_dice.count(biggest)):
                picked_dice.append(biggest)
        else:
            picked_dice.append(biggest)

        return picked_dice

    def get_results(self, dice):
        '''
        Get the score of the saved dice. The qualifying 1 and 4 are not counted. 
        If the player does not qualify the score is 0. 
        '''
        result = 0
        if dice is None:
            dice = self.saved_dice

        if 1 in dice and 4 in dice:
            while len(dice) is not 0:
                result = result + dice.pop()

            result = result - 5 # subtract 5 for the 1 and 4 when qualified

        self.results = result
        return result

    def play(self):

        while len(self.saved_dice) is not 6:
            self.thrown_dice = self.dice.roll(6 - len(self.saved_dice))

            # Look for a one or four, take one and roll again
            if self.qualified is False:
                if 1 in self.thrown_dice and 1 not in self.saved_dice:
                    self.save_dice([1])

                if 4 in self.thrown_dice and 4 not in self.saved_dice:
                    self.save_dice([4])

            if(len(self.thrown_dice) is not 0):
                # Get the biggest dice in the roll
                if 6 in self.thrown_dice:
                    biggest = self.pick_highest(True)
                    self.save_dice(biggest)
                else:
                    biggest = self.pick_highest()
                    self.save_dice(biggest)
                
            # Are we qualified?
            if 1 in self.saved_dice and 4 in self.saved_dice:
                self.qualified = True
        
        self.get_results(self.saved_dice)