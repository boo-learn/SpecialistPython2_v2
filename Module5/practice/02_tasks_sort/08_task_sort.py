# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

def sort_choice(nums):
    i = 0
    global count
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        #count += 1
        i += 1

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
short_phones = []
for phone in phones:
    short_phone = phone.replace("-", "")
    short_phones.append(short_phone)
sort_choice(short_phones)
phones = []
for short_phone in short_phones:
    phones.append('-'.join(short_phone[i:i+2] for i in range(0, len(short_phone), 2)))
print(phones)
