# Возьмите алгоритм сортировки пузырьком из examples/bubble_sort.py
# Раскомментируйте print-ы, изучите вывод в консоли.
# Вспомнив теорию, оптимизируйте алгоритм сортировки...

nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
len_number = len(nums) - 1
while swapped:    
    swapped = False
    # print("*****")
    for i in range(len_number):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
            len_number -=1
print("after sort = ", nums)
