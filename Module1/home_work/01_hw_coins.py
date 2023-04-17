import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        """
        Подбрасывание монетки. # heads-орел/tails-решка
        """
        coin_variants = ("heads", "tails")
        self.side = random.choice(coin_variants)


# 1. Создайте список из n-монеток, n - вводится с клавиатуры
n = int(input("Введите количество монет n: "))
coins = []
i = 0
while i < n:
    new_coin = Coin()
    coins.append(new_coin)
    i += 1

# 2. Подбросьте(flip) все монетки. У каждой монетки в списке вызовите метод .flip()
for current_coin in coins:
    current_coin.flip()

# 3. Выведите соотношение выпавших орлов и решек в процентах
side_heads = 0
side_tails = 0

# Количество каждой из сторон
for current_coin in coins:
    if current_coin.side == "heads":
        side_heads += 1
    else:
        side_tails += 1

# Получение доли в процентах
if side_heads == 0:
    side_heads_part = 0
    side_tails_part = 100
elif side_tails == 0:
    side_tails_part = 0
    side_heads_part = 100
else:
    side_heads_part = side_heads / (side_heads + side_tails) * 100
    side_tails_part = side_tails / (side_heads + side_tails) * 100

# Показать стороны случайных монет
for c in coins:
    print(c.side)

print(f"Соотношение выпавших сторон: 'орёл' - {side_heads_part:.02f}%, 'решка' - {side_tails_part:.02f}%")
