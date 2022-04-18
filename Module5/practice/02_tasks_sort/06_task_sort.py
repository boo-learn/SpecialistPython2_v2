import random

incoming_list = []
N = random.randint(2, 10)
for i in range(N):
    incoming_list.append(random.randint(1, 50))

incoming_list.sort()
new_list = []

while len(incoming_list) != 0:
        new_list.append(incoming_list.pop(-1))
        new_list.append(incoming_list.pop(0))

print(new_list)
print(sum(new_list[0::2]))
