nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)

swapped = True
length_list = len(nums)
while swapped:
    swapped = False
    print("*****")
    for i in range(length_list - 1):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
    length_list -= 1

print("after sort = ", nums)
