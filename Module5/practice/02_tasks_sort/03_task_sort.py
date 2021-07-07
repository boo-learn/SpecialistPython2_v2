# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов


def gen_list(size, at=-100, to=100):
    import random
    return [random.randint(at, to) for _ in range(size)]

def sort_choice(nums):
    i = 0
    count = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            count += 1
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

c=14
num = gen_list(c)
sum_ = 0
i=0
print(num)
sort_choice(num)
print(num)
num_ = num[c-10:]
for i in range(len(num_)):
        sum_ += num_[i]
        i += 1
print(sum_)
