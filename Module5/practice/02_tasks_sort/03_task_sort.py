numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
# numbers = [5, 2, 5, -5, 4, 5, 1, -5, 4, 5, 0]

numbers.sort()
print(numbers)
s = 0
for num in numbers[-5:]:
    s += num
print(s)
