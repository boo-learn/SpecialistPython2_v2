# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.


stones = [44, 34, 1, 56,5, 2, 1, 8, 4, 12, 23, 8, 30]
stones1 = []
stones2 = []

print(stones)
stones.sort()
print(stones)
flag = 0
for i in range(0, len(stones)):
    sum1 = 0
    sum2 = 0
    #print(stones[i])
    for j in range(0, i): sum1 += stones[j]
    for j in range(i+1, len(stones)): sum2 += stones[j]
    print("****")
    if sum1 * 2 >= sum2 and sum2 > sum1:
        print(sum1, ",", sum2)
        for n in range(0, i): stones1.append(stones[n])
        for n in range(i+1, len(stones)): stones2.append(stones[n])
        flag = 1
if flag ==1:
    print(stones1)
    print(stones2)
else:
    print(stones)
