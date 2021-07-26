# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

stone=[2,3,4,2,1,15,2,8,9,16]
if max(stone)>(sum(stone)-max(stone))*2:
    print ("Невозможно")
else:
    stone.sort()
    sum_small=1
    sum_big=max(stone)
    i=0
    while sum_big/sum_small>2:
        sum_small=sum(stone[:i+1])
        sum_big=sum(stone[i+1:])
        i+=1
    print(stone[:i])
    print(stone[i:])
