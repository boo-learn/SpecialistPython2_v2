numbers = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1]


def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1


a = []
bubble_sort(numbers)
print(numbers)
a = list(set(numbers))
bubble_sort(a)
print(a)
a.reverse()
print(a)
s = 0
for i in range(3):
    s += numbers.count(a[i])

print('Призеров ', s)
