# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
int_phones=[]

for phone in phones:
    int_phones.append(int(phone.replace("-","")))
    int_phones.sort()
    phones=[]
for phone in int_phones:
    phone=str(phone)
    new_phone=f"{phone[:2]}-{phone[2:4]}-{phone[4:]}"
    print(new_phone)
    phones.append(new_phone)
print(phones)
