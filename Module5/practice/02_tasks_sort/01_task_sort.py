# Сумма с условием
# Дан массив(список) чисел.
# Найти: сумму элементов массива, больших данного числа А


# Возьмите алгоритм сортировки пузырьком из examples/bubble_sort.py
# Раскомментируйте print-ы, изучите вывод в консоли.
# Вспомнив теорию, оптимизируйте алгоритм сортировки...

# nums = [-5, 2, 2, 1, 8, 477]
print("before sort = ", nums)
j = 0
swapped = True
while swapped:
    swapped = False
    # print("*****")
    for i in range(len(nums) - 1-j):
        # print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)



#!!!!!!!!!!не рабочий код. Не знаю как елементы изолировать. 
