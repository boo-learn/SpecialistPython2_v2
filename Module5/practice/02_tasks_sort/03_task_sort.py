import random
def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1

def gen_list(size, at=-100, to=100):
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))

    return data


l1 = gen_list(15)
print(l1)
bubble_sort(l1)
print(l1)
s = 0
for el in l1[-10:]:
    s+=el
print(s)
