def phone_to_number(phone):
    phone = int(phone[:2] + phone[3:5] + phone[6:8])
    return phone

def number_to_phone(phone):
    phone = str(phone)
    phone = phone[:2] + '-' + phone[2:4] + '-' + phone[4:6]
    return phone

def choice_sort(nums, reverse = False, key = lambda n: n):
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

        
phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

phones = [phone_to_number(phone) for phone in phones]
choice_sort(phones)
phones = [number_to_phone(phone) for phone in phones]

print(phones)


# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67
