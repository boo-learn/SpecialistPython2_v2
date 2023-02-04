from base_sort import sort_choice
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
# Вход:дано N натуральных чисел – цены товаров.
#вводим числа через input, переводим в массив чисел, сортируем его и разворачиваем.
results = input("Введите результаты участников: ")
results_arr = []
results_arr = results.split(" ")
for i in range(len(results_arr)):
    results_arr[i] = int(results_arr[i])
sort_choice(results_arr)
results_arr.reverse()

result_old = 0
leaders_number = 0
diplom_numbers = 0
for result in results_arr:
    if result != result_old:
        result_old = result
        diplom_numbers += 1
        if diplom_numbers == 4:
            break
        else:
            leaders_number += 1
    elif result == result_old:
        result_old = result
        leaders_number += 1

print(leaders_number)
