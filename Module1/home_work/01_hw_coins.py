import random

class Coin:
    def __init__(self, n):
        # heads-орел/tails-решка
        self.side = None
        self.list_coins = [f'C{i}' for i in range(n)]
        
    def flip(self):
        result_ = [random.choice(['heads','tails']) for i in self.list_coins]
        self.side = result_.count('heads')/result_.count('tails')
        return self.side
