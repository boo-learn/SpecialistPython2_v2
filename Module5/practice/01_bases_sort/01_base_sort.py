# Возьмите алгоритм сортировки пузырьком из examples/bubble_sort.py
# Раскомментируйте print-ы, изучите вывод в консоли.
# Вспомнив теорию, оптимизируйте алгоритм сортировки...

nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)

n = len(nums)
swapped = True

while swapped:
    swapped = False

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
      
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
            swapped = True
    n -= 1
    if not swapped:
        break

print("after sort = ", nums)
