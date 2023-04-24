def sum_os_nubbers(digit, second_digit):
    numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
    summ = 0# ...  # Задайте самостоятельно, выбрав произвольное число
    for num in numbers:
        if digit < num < second_digit:
            summ += num
    return summ
