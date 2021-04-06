import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        side = ('heads', 'tails')
        self.side = random.choice(side)  # random: heads/tails

num = 99999
coin_list = []

for n in range(num):
    cos = Coin()
    cos.flip()
    coin_list.append(cos)

num_h = 0
num_t = 0

for m in coin_list:
    if m.side == 'heads':
        num_h += 1
    else:
        num_t += 1

print(f'количество орлов: {num_h}, количество решек: {num_t}')
