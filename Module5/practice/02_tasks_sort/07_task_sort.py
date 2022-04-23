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
def winners(quantity, participants):
    summ = 0
    participants.sort(reverse=True)
    dict_winners = {}
    for participant in participants:
        dict_winners.update({participant: participants.count(participant)})
    if quantity <= 3:
        return sum(dict_winners.values())
    keys = list(dict_winners.keys())
    for i in range(3):
        summ += dict_winners.get(keys[i])
    return summ




print(winners(10, [1, 3, 4, 3, 5, 6, 7, 7, 6, 1]))
