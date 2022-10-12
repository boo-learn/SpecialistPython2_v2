nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
n = len(nums) - 1
while swapped:
    swapped = False
    print("*****")
    for i in range(n):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    n -= 1
print("after sort = ", nums)
