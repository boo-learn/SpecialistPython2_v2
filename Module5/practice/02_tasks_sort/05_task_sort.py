staff.sort(key = lambda emp: (emp["salary"], emp["surname"]))
# print(staff)

res = sum(map(lambda emp: emp["salary"], staff[:3]))
print(res)

sum_salary = 0
for emp in staff[:3]:
    sum_salary += emp["salary"]
print(res)
