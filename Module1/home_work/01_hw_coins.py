import random, sys
'''
Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
выведите соотношение выпавших орлов и решек в процентах
'''


class Coin:
    HEADS = "Heads"
    TAILS = "Tails"

    def __init__(self):
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice([Coin.HEADS, Coin.TAILS])
        if self.side == Coin.HEADS:
            return True

    def to_str(self, ind):
        return f"Coin#{ind}: {self.side}"


# Get the list lenght from user
try:
    coin_count = int(input('Please, add coin\'s count (default - 4): ') or '4')
    if coin_count <= 0:
        sys.exit(1)
except:
    print("Error: Integer and gt 0")
    sys.exit(1)


coin_ind = 0
coin_heads_count = 0
# Create class instances according to coins count
for coinN in range(coin_count):
    coinN = Coin()  # Можно ли создать экз класса и использовать метод в 1-ну строку?
    if coinN.flip():
        coin_heads_count += 1
    coin_ind += 1
    print(coinN.to_str(coin_ind))

# Calculate %
heads_per = round(coin_heads_count / coin_count * 100, 2)
tails_per = round(100 - heads_per, 2)

# Show results
print("Heads count: ", heads_per, "%")
print("Tails count: ", tails_per, "%")
