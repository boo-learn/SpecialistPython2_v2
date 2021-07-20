count_coins = int(input('Введите количество монеток: '))

coins_list = []
count = 0
while count < count_coins:
    coins_list.append(Coin())
    count += 1

fliped_coins = list(map(Coin.flip, coins_list))

f_count = 0
h_count = 0
for i in fliped_coins:
    if i == 'heads':
        h_count += 1
    else:
        f_count += 1

print(f'Соотношение орлов и решек составляет {h_count/count_coins*100} к {f_count/count_coins*100}')
