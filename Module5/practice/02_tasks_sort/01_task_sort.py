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

def gen_list(size, at=-10, to=10):
    import random
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    return [random.randint(at, to) for _ in range(size)]

A = 5
s = 0
l = gen_list(10)
sort_choice(l)
print('l = ', l)
for i in l:
    if i >= A:
        s += i
print('sum; ', s)
