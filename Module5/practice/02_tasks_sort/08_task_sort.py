def sort_choice(nums, reverse = False):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            a = nums[j]
            b = nums[m]
            condition = a < b
            if reverse:
                condition = condition = a > b
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    # print("sort_choice, after sort = ", nums)

# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58","55-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
phones.sort()
print(phones)

phones = ["25-17-58","55-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
sort_choice(phones)
print(phones)


