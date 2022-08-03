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


def count_winners(n, *participants) -> int:
    """
    Определить количество призеров олимпиады
    :param n: число участников
    :param participants: баллы участников
    :return: число призеров олимпиады
    """
    if n != len(participants):
        raise ValueError(f'Число участников не равно {n}!')
    participants = list(participants)
    participants.sort()
    winners_list = list(set(participants))[:3]
    counter = 0
    for participant in participants:
        if participant in winners_list:
            counter += 1
        else:
            break
    return counter


winners = count_winners(10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1)
print(winners)
