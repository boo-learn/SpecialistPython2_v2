import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        side_tuple = ('heads', 'tails')
        self.side = random.choice(side_tuple)  # random: heads/tails

        
coin_list = []
flip_results_dict = {'heads':0, 'tails':0}

quantity_of_coins = int(input('Enter quantity of coins you need: '))

for i in range(quantity_of_coins):
    coin = Coin()
    coin_list.append(coin)

print(flip_results_dict.keys())


for value in coin_list:
    value.flip()
    if value.side == 'heads':
        flip_results_dict['heads'] +=1
    else:
        flip_results_dict['tails'] +=1

print('Процентное соотношение выпавших орлов {:.2f}'.format((flip_results_dict['heads'] / quantity_of_coins) * 100))
print('Процентное соотношение выпавших решек {:.2f}'.format((flip_results_dict['tails'] / quantity_of_coins) * 100))
# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
