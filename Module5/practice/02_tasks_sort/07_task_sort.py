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
winners = [1, 3, 4, 3, 5, 6, 7, 7, 6, 1]

winners_set = set(winners)
winners_sorted = sorted(winners_set, reverse=True)


count = 0
for winner in winners:
    if winner in list(winners_sorted)[:3]:
        count += 1

print(count)
