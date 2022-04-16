price_list = []
n = int(input('Vvedite число товаров (N < 1000): '))
for i in range(n):
    if n < 1000:
        price = int(input(f'Vvedite цены товаров {n-i} раза: '))
        price_list.append(price)
    i += 1

print(price_list)

price_list.sort... # застрял...
