import random


class Coin:
    def __init__(self):
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        sides = ['heads', 'tails']      # heads-орел/tails-решка
        self.side = random.choice(sides)  # random: heads/tails
        return self.side


count = int(input("Введите количество монет: "))
coins = []
heads = 0
tails = 0
while count > 0:
    coins.append(Coin())
    count -= 1
sides_coins = []
for coin in coins:
    sides_coins.append(coin.flip())
for char in sides_coins:
    if char == 'heads':
        heads += 1
    if char == 'tails':
        tails += 1
count = heads + tails

print(f'Орёл выпал в {heads * 100 / count}% подбрасывания монетки')
print(f'Решка выпала в {tails * 100 / count}% подбрасывания монетки')
