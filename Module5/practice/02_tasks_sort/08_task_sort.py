# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

def sort_choice(nums):
    i = 0
    # count = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            # count += 1
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    # print(f'{count=}')

print(phones)
sort_choice(phones)
print(phones)

phones2 = ["25-10-01", "25-10-02", "25-10-03", "25-11-01", "25-12-03", "21-12-03"]
print(phones2)
sort_choice(phones2)
print(phones2)
