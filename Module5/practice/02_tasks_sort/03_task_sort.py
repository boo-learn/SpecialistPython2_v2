# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

sum = 0
for i in range(5):
    max = numbers[1]
    index_max = 0
    i = 0
    for num in numbers:
        if num > max:
            max = num
            index_max = i
        i += 1
    sum = sum + max
    numbers.pop(index_max)

print(f"SUM = {sum}")

stri = ''
for num in numbers:
    stri = stri + ',' + str(num)
print(stri[1:])
