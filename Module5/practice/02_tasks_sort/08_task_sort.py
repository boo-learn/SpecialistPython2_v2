# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]


def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums


if __name__ == '__main__':
    print(bubble_sort(phones, key=(lambda x: int(x.replace('-', '')))))
