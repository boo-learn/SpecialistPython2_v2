import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        if random.randint(0,1):
            self.side = 'heads'
        else:
            self.side = 'tails'

        return self.side   # random: heads/tails


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())

n = random.randint(1,100)

coins = []

for _ in range(n):
    coins.append((Coin()))

tails = heads = 0

for coin in coins:
    if Coin.flip(coin) == 'heads':
        heads += 1
    else:
        tails += 1

print(f'total number of flips - {n}')
print(f'% of tails - {round((tails / (heads+tails) * 100),2)}%')
print(f'% of heads - {round((heads / (heads+tails) * 100),2)}%')
