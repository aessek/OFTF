from OFTF import OFTF
import numpy

outcomes = list()
for i in range(1000):
    game = OFTF()
    game.play()
    outcomes.append(game.results)

print('# of games played: {}'.format(len(outcomes)))
print('Result \t\t# times rolled')
for i in range(0, 25):
    print('{}: \t\t{}'.format(i, outcomes.count(i)))

print('Average: {}'.format(numpy.mean(outcomes)))