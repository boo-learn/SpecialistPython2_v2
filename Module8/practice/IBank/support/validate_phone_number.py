import re

phone_numbers = ["+7-900-620-10-20", "8-900-620-10-20", "+7-90-62-10-20", "+7 900 620 10 20", "+7-100-100-11-22"]
pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

for phone_number in phone_numbers:
    if re.match(pattern, phone_number):
        print(f"Passport number {phone_number} is correct")
    else:
        print(f"Passport number {phone_number} is not correct")