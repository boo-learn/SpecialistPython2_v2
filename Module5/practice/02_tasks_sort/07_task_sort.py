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

def create_check(list_inval: list):
    sort_list = list_inval[:]
    sort_list.sort(reverse=True)
    print(sort_list)
    flag_ = len(sort_list) // 2
    big_list = sort_list[:flag_]
    low_list = sort_list[flag_:]
    result = list()
    if len(low_list) > len(big_list):
        big_list.append(low_list[0])
        del low_list[0]
        for i in range(len(big_list)-1):
            result.append(big_list[i])
            result.append(low_list[i])
        result.append(big_list[-1])
    else:
        for i in range(len(big_list)):
            result.append(big_list[i])
            result.append(low_list[i])
    print(result)
    summ = int()
    for i in range(0, len(result), 2):
        summ += result[i]
    return summ


if __name__ == '__main__':
    inval_list = [5, 2, 1, 10, 50, 5, 5, 1]
    print(create_check(inval_list))
