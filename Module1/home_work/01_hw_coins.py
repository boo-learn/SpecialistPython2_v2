import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        sides = ('heads', 'tails')
        self.side = random.choice(sides)
        return self.side

coin1 = Coin()
coin2 = Coin()
coin3 = Coin()
coin4 = Coin()
coin5 = Coin()
coin6 = Coin()
coin7 = Coin()
coin8 = Coin()
coin9 = Coin()
coin10 = Coin()

coins = [coin1, coin10, coin9, coin8, coin7, coin6, coin5, coin4, coin3, coin2]
def heads_at_tails(lst):
    head = 0
    tail = 0
    for el in lst:
        if el.flip() == 'heads':
            head +=1
        else:
            tail +=1
    return f'Соотношение heads = {(head/len(lst))*100}%, tails = {(tail/len(lst))*100}%'


print(heads_at_tails(coins))

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
