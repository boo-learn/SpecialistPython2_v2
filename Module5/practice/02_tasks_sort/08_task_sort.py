# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    return nums


phones = ["25-17-58", "11-34-85", "54-61-56",
          "34-61-72", "25-17-55", "34-56-56"]
phone_int = []
phones_sort = []

print(phones)

for num in phones:
    n = num.split("-")
    phone_int.append(list(map(int, n)))

nums = sort_choice(phone_int)

for n in nums:
    phones_sort.append("-".join(str(_) for _ in n))
print(phones_sort)
