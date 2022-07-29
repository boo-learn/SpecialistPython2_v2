numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 7  # Задайте самостоятельно, выбрав произвольное число

sum_num = 0
for num in numbers:
    if num > a:
        sum_num += num
print(f'Сумма чисел больше, чем число {a} = {round(sum_num, 1)}')
