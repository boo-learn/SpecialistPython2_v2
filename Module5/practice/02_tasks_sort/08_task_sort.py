# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

def sort_choice(nums, reverse=False, key=lambda n: n):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1

        while j < len(nums):
            if reverse:
                condition = key(nums[j]) > key(nums[m])
            else:
                condition = key(nums[j]) < key(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


sort_choice(phones, reverse=True)

print(phones)
