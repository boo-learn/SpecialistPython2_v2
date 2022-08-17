numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10

b = 20
s = []
for i in range(len(numbers)):
    if numbers[i] > a and numbers[i] < b:
        s.append(numbers[i])

print(sum(s))
