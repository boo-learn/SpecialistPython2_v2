# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]

def bubble_sort(nums: list, key=lambda x: x, reverse=False):
    swapped = True
    offset = 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - offset):
            # print("i = ", i)
            if reverse:
                exp = key(nums[i]) < key(nums[i + 1])
            else:
                exp = key(nums[i]) > key(nums[i + 1])
            if exp:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации

                swapped = True
        offset += 1

bubble_sort(phones, key=lambda x: x.split('-'))

print(phones)
