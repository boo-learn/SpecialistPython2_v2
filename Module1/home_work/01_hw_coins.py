import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(("Head", "Tail"))  # random: heads/tails

coin_list = []
for i in range(1, 10):
    coin_list.append(Coin)

flip_list = []
for coin in coin_list:
    coin.flip(Coin)
    flip_list.append(coin.side)
    
print(flip_list)
print(f"Выпало орлов: {round(100*(flip_list.count('Head'))/len(coin_list), 2)}%, решек: {round(100*(flip_list.count('Tail'))/len(coin_list), 2)}%.")

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки,
# выведите соотношение выпавших орлов и решек в процентах.

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
