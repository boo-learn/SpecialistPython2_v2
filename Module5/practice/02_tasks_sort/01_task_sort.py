numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 0
sum = 0
for i in range(len(numbers)-1):
    if numbers[i]>a:
        sum = sum + numbers[i]
print(f"{sum=}")
