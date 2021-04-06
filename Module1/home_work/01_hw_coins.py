import random

class Coin:
    def __init__(self, side):
        self.side = side

    def __repr__(self):
        return self.side

    def flip(self):
        self.side = 'head' if random.random() >= 0.5 else 'tail'

coins = []

for _ in range(random.randint(1, 15)):
    side = 'head' if random.random() >= 0.5 else 'tail'
    coins.append(Coin(side))

heads = 0

for coin in coins:
    coin.flip()
    if coin.side == 'head':
        heads += 1

heads_percent = round(heads/len(coins)*100)
tails_percent = 100 - heads_percent
    
print(coins)

print(f'heads: {heads_percent}%, tails: {tails_percent}%')

## Список из n монет head tail 
## Каждую подбросить и в процентах вывести соотношение

