import random


def gen_list(size, at=0, to=100):
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))

    return data

l1 = gen_list(10)
print(l1)
a = 10
b = 50
sum = 0
for i in l1:
    if b > i > a:
      sum += i

print(sum)
