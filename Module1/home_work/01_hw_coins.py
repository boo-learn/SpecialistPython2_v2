import random

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['head','tail'])

# Бондаренко Владимир

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
n = int(input('Enter count coins: '))
coins = []
i = 0
while i < n:
    unit_coin = Coin()
    coins.append(unit_coin)
    i += 1
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
for coin in coins:
    coin.flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах
head_count = 0
tail_count = 0
for coin in coins:
    if coin.side == 'head': head_count += 1
    else: tail_count +=1

print('Орлов выпало '+str(head_count)+' из '+ str(head_count+tail_count) +', что составляет ' + str(round(head_count/n*100, 2)) + '%')
print('Решек выпало '+str(tail_count)+' из '+ str(head_count+tail_count) +', что составляет ' + str(round(tail_count/n*100, 2)) + '%')

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
