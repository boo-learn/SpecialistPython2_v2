def sort_choice(nums):
    from random import randint

    # Алгоритм:
    # 1. Найти наименьшее значение в списке.
    # 2. Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
    # 3. Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
    # 4. Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
    # 5. Продолжать выполнять поиск и обмен, пока не будет достигнут конец списка.

    # nums = [5, 2, -1, 8, 4, -4, 7]
    print("sort_choice, before sort = ", nums)
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    print("sort_choice, after sort = ", nums)

# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 6.7  # Задайте самостоятельно, выбрав произвольное число
numbers.append(a)
sort_choice(numbers)

numbers1 = numbers[numbers.index(a)+1:]
for n, item in enumerate(numbers1):
    if item == a:
        numbers1.pop(n)

res = sum(numbers1)
print(f'{res = }')
