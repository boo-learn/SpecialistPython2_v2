# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10

check = [5, 2, 1, 10, 50, 10, 9, 7, 40]
check_prices = check[1:]
check_prices.sort()
final_check = []
summa = 0
for i in range(len(check_prices)//2):
    final_check.append(check_prices[len(check_prices) - 1 - i])
    summa += check_prices[len(check_prices) - 1 - i]
    final_check.append(check_prices[i])
if len(check_prices) % 2 != 0:
    final_check.append(check_prices[len(check_prices) //2])
    summa += check_prices[len(check_prices) //2]
print(final_check)
print(summa)
