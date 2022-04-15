numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
for i in range(len(numbers)-1):
    for j in range (len(numbers)-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
summa=0
for i in range(len(numbers)-5,len(numbers),1):
    summa+=numbers[i]

print(summa)
