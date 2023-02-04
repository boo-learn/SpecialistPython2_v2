# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
from base_sort import sort_choice

# Вход:дано N натуральных чисел – цены товаров.
#вводим числа через input, переводим в массив чисел, сортируем его и разворачиваем.
prices = input("Введите цены: ")
prices_arr = []
prices_arr = prices.split(" ")
for i in range(len(prices_arr)):
    prices_arr[i] = int(prices_arr[i])
sort_choice(prices_arr)
prices_arr.reverse()

# Выход: одно число – максимальная сумма чека.
#Проверяем количество чисел в массиве. Если чётное - берем первую половину чисел. Если нечетное - на одно больше. Суммируем.
sumv = 0
numbers_count = 0
if len(prices_arr) % 2 == 0:
    numbers_count = len(prices_arr)/2
else:
    numbers_count = (len(prices_arr) + 1) / 2
for i in range(int(numbers_count)):
    sumv += prices_arr[i]
print(sumv)
