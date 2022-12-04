import random
n = int(input())
coins_list = []
head_list = []
i = n
class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        random_list = ['head', 'tail']
        random_choice = random.choice(random_list)
        return random_choice
while n <= 0:
    print('Количество монет не может быть отрицательным или равняться нулю!')
    n = int(input())
while i > 0:
    coins_list.append(Coin.flip(0))
    i -= 1
for coin in coins_list:
    if coin == 'head':
        head_list.append(coin)
print(f"Аверс: {((len(head_list)*100)//n)} %, Реверс: {100-(len(head_list)*100)//n}%")
