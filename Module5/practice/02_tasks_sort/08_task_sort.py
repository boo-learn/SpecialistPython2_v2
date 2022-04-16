# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
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


def number_format(stroka):
    stroka_2 = str()
    for i in range(len(stroka)):
        stroka_2 += stroka[i]
        if i % 2 != 0 and i != len(stroka) - 1:
            stroka_2 += "-"
    return stroka_2


phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
list_phones = []

for phone in phones:
    list_phones.append(phone.replace("-", ""))
sort_choice(list_phones)

for i in range(len(list_phones)):
    list_phones[i] = number_format(list_phones[i])

print(list_phones)
