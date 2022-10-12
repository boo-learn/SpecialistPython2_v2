# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5

import random

n = 11
points = [random.randint(0, 10) for _ in range(n)]
print(points)

points.sort(reverse=True)
print(points)

prize = points[0]
diploma = 1
num_prizes = 0
for point in points:
    if point >= prize:
        num_prizes += 1
    else:
        prize = point
        diploma += 1
        if diploma <= 3:
            num_prizes += 1
        else:
            break
print(num_prizes)

