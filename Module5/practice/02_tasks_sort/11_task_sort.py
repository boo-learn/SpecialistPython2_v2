def sort_choice(nums: list) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


anagrams = ["роза", "азор", "озра", "карт",
            "тарк", "трак", "кошка", "кишка", "кашка", "машка"]
new_anag = []
dict_anag = {}

for i in anagrams:
    value = []
    value += i
    sort_choice(value)
    value = "".join(value)
    key = i
    if not dict_anag.get(value):
        dict_anag[value] = [key]
    else:
        dict_anag[value].append(key)

j = 1
for value in dict_anag.values():
    if len(value) > 1:
        print(f"Группа анаграмм {j}: {value}")
        j += 1
