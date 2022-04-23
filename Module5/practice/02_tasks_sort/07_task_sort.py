scores = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1,6,10]
scores = sorted(scores, reverse= True )
print(scores)
i = 0
j = 0
for i in range(len(scores)):
    if scores[i] != scores[i+1]:
        j += 1
        if j == 3:
            break
print(i+1)
