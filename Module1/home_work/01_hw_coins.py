import random


class Coin:
    sides = ("heads", "tails")
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """
        Подбрасывание монетки
        """
        self.side = random.choice(Coin.sides)


# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах


def generate_coin_list(num_coins):
    coin_list = []
    for i in range(num_coins):
        coin_list.append(Coin())
    return coin_list


def flip_coins_from_list(coin_list):
    for coin in coin_list:
        coin.flip()


def count_flip_result(coin_list):
    num_heads = 0
    num_tails = 0
    for coin in coin_list:
        if coin.side == "heads":
            num_heads += 1
        elif coin.side == "tails":
            num_tails += 1
        else:
            print("Warning: coin not flipped yet.")
    
    heads_percent = num_heads / len(coin_list) * 100
    tails_percent = num_tails / len(coin_list) * 100
    
    print(f"Result: {round(heads_percent, 2)}% heads, {round(tails_percent, 2)}% tails.")


def main():
    coins = generate_coin_list(99)
    flip_coins_from_list(coins)
    count_flip_result(coins)


if __name__ == "__main__":
    main()
