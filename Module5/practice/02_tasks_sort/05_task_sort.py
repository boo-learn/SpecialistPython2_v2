staff.sort(key=lambda n: n['salary'])
staff_list = []
sal_list = []

for emp in staff:
    staff_list.append(emp['surname'])
    sal_list.append(emp['salary'])

print(staff_list)
print('Сумма зарплат трех самых низкооплачиваемых сотрудников:')
print(sum(sal_list[:3]))
