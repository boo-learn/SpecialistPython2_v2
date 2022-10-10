import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])  # random: heads/tails

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())


n = int(input('Введите число монеток: '))
coins = [Coin() for _ in range(n)]
num_heads = 0
num_tails = 0
for coin in coins:
    coin.flip()
    if coin.side == 'heads':
        num_heads += 1
    elif coin.side == 'tails':
        num_tails += 1
percent_heads = num_heads/n*100
percent_tails = num_tails/n*100
print(f'Выпало {percent_heads}% орлов и {percent_tails}% решек')
