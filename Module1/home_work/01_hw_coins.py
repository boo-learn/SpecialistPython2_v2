import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        self.side = random.choice(['heads', 'tails'])

n = int(input("Введите количество монеток: "))
coins = [Coin() for _ in range(n)]

for coin in coins:
    coin.flip()

heads_count = sum(coin.side == 'heads' for coin in coins)
tails_count = n - heads_count

print(f"Орлов {heads_count/n*100:.2f}%")
print(f"Решек {tails_count/n*100:.2f}%")
# print(f"{heads_count/n*100:.2f}% орлов - {tails_count/n*100:.2f}% решек")

# Задание:
# 1. Создайте список из n-монеток, n - вводится с клавиатуры
# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
# 3. Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
