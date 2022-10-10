import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.randint(1, 2)  # random: heads/tails
        if self.side == 1:
            check = 'орел'
        else:
            check = 'решка'
        return check
# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
n = int(input('ввести количество монет: '))
list_coin = []
for i in range(n):
    list_coin.append(Coin())
ver = []
for i in list_coin:
    ver.append(i.flip())
print(f'Процент появления решка - {(ver.count("решка")/n*100)}%')
print(f'Процент появления орла - {ver.count("орел")/n*100}%')
