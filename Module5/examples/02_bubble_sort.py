nums = [5, 2, 1, 8, 4]
print("before sort = ", nums)
swapped = True
end = len(nums)
while swapped:
    swapped = False
    end -= 1
    print("*****")
    for i in range(end):
        print("i = ", i)
        if nums[i] > nums[i + 1]:
            # Меняем элементы
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            # Устанавливаем swapped в True для следующей итерации
            swapped = True
print("after sort = ", nums)
