import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка

        """
        sides = ['heads', 'tails']
        result = random.choice(sides)
        self.side = result  # random: heads/tails
        return self.side


# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
number = int(input('Введите количество монеток: '))
l1st = range(int(number))
coin_list = []
for coin in l1st:
    coin_list.append(Coin)

# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
flip_list = []
for coin in coin_list:
    flip_list.append(coin.flip(coin))


# 3. Выведите соотношение выпавших орлов и решек в процентах
heads = []
tails = []
for coin in flip_list:
    if coin == 'heads':
        heads.append(coin)
    else:
        tails.append(coin)
result_heads = 100 / number * len(heads)
result_tails = 100 / number * len(tails)
print('Орлов: ', result_heads, '%', 'Решек: ', result_tails, '%')

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
