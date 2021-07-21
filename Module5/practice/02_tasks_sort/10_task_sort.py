# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

import random


def gen_weights(num, at=0, to=20):
    random.seed(10)
    weights = []
    for _ in range(num):
        weights.append(random.randint(at, to))
    return weights


amount = 7
weights = gen_weights(amount)
print(weights)
weights.sort(reverse=True)
print(weights)

group_2 = []
group_1 = []
i = 0
j = 1
while i < len(weights) - 1:
    group_2.append(weights[i])
    group_1.append(weights[j])
    i += 2
    j += 2

print(group_2)
print(group_1)
sum_1 = sum(group_1)
sum_2 = sum(group_2)
if sum_1/sum_2 > 2:
    print("Can't divide it")
print(f" Two stack with weights:{sum_1} and {sum_2}")
