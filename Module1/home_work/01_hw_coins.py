import random

coins = ['орел', 'решка']


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(coins)
        return self.side


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
heads, tails = 0, 0

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
count = int(input('Введите целое число, сколько раз подбросить монетку: '))

side = Coin()

for _ in range(count):
    planted = side.flip()
    if planted == 'орел':
        heads += 1
    else:
        tails += 1
print(f'Орлов выпало: {round(((heads * 100) / count), 2)}%, Решек выпало: {round(((tails * 100) / count), 2)}%')
