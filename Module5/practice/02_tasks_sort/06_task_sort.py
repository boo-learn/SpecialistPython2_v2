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


def count_winners(score_list):
    cw = 0
    score_list.sort(reverse=True)
    s_prev = score_list[0]
    num_win_positions = 3
    for score in score_list:
        if score == s_prev:
            cw += 1
        else:
            num_win_positions -= 1
            if num_win_positions > 0:
                cw += 1
                s_prev = score
            else:
                break
    return cw

N = 20
array = [random.randint(1, 20) for _ in range(N)]
print(array)
print(f"We have {count_winners(array)} winners.")
print(array)
