import random

heads = 0
tails = 0
count = 0
while count != 100:
    coin = random.randint(1, 2)
    count += 1
    if coin == 1:
        heads += 1

    elif coin == 2:
        tails += 1


print(f'Орел {heads}%')
print(f'Решка {tails}%')
