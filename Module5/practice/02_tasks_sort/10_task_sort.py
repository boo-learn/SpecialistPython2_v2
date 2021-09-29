stones = [1000, 5, 4, 45, 12, 122]

# for i in range(10):
#     stones.append(randint(1, 5000))
# print(stones)

stones.sort(reverse=True)
print(stones)
loot_1 = []
loot_2 = []

for stone in stones:
    if sum(loot_1) > sum(loot_2):
        loot_2.append(stone)
    else:
        loot_1.append(stone)
print(loot_1)
print(loot_2)
print(sum(loot_1))
print(sum(loot_2))
if ((sum(loot_1))/2) > sum(loot_2) or ((sum(loot_2))/2) > sum(loot_1):
    print("невозможно разделить")
else:
    print("разделение возможно")
