import re

passport_numbers = ["3200 123456", "3200 12345" , "hello", "320! 12345", "1234 654321"]
pattern = r"\d{4} \d{6}"

for passport in passport_numbers:
    if re.match(pattern, passport):
        print(f"Passport number {passport} is correct")
    else:
        print(f"Passport number {passport} is not correct")