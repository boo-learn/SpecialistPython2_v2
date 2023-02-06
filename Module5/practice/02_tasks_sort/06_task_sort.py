import random as r
n = 10
# создаем список из случайных чисел от 1 до 15 в количестве n
cost_list = [r.randint(1, 15)for _ in range(n)]
# сортируем список цен
cost_list.sort(reverse=True)
# инвертируем что бы самые дорогие товары были первыми
# список в который будем записывать результат
res_list = []
if n % 2 != 0:  # если товаров не четное количество
    res_list.append(cost_list[0])
    cost_list = cost_list[1:]
    for i in range(len(cost_list)//2):
        res_list.append(cost_list[-1-i])
        res_list.append(cost_list[i])
else:  # если товаров четное количество
    for i in range(len(cost_list)//2):
        res_list.append(cost_list[i])
        res_list.append(cost_list[-1-i])

print(cost_list)
print(res_list)
max_check = 0
for k in range(0, n, 2):
    max_check += res_list[k]
print(max_check)
