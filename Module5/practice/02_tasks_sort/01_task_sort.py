numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]

a = int(input())
rez=0
for i in numbers:
    if  i>a:
        rez+=i

print(rez)
