# Сумма из диапазона
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А, но меньше B.


def gen_list(size, at=-100, to=100):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]


if __name__ == '__main__':
    a = 5
    b = 100
    s = 0
    nums = gen_list(10)
    print(nums)

    for num in nums:
        if num > a and b > num:
            s += num

    print(s)
