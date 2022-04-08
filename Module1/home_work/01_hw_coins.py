import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = 'heads' if random.randint(0,1) else 'trails'  # random: heads/tails

# спрашиваем количество подброшенных монеток
while True:
    try:
        n = int(input("Сколько монеток хотите подбросить: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print(f"{n} - это не целое положительное число")

# создаем список монеток и подбрасываем каждую
coins = [Coin() for x in range(0, n)]
for coin in coins:
    coin.flip()

# Считаем количество орлов
heads = 0
for coin in coins:
    if coin.side == 'heads':
        heads += 1

# подсчитываем проценты орлов и решек и выводим их
heads_procent = heads * 100 / len(coins)
trails_percent = (len(coins) - heads) * 100 / len(coins)
print(f"Процент орлов {heads_procent}%, процент решек {trails_percent}%")


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# она находится у вас в руке и не выпала ни орлом ни решкой. Монетка "определеяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())
