# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]


def phone_format(phone):
    return int(phone.replace("-", ""))


def sort_choice(nums: [], rule: lambda n: n) -> []:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if rule(nums[j]) < rule(nums[m]):
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    return nums


print(phones)
sort_choice(phones, rule=phone_format)
print(phones)
