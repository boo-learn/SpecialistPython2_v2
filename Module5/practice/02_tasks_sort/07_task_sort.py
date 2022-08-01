result_list = [7, 7, 7, 4, 5, 6, 6, 7, 1, 8]

result_list.sort()
result_list.reverse()

print(result_list)

i = 0
j = 0
res = 0

while i < 3:
    j = 0
    while j < len(result_list):
        if j == len(result_list) - 1:
            res = res + result_list.count(result_list[j])
            result_list = []
        elif result_list[j] > result_list[j + 1]:
            res = res + result_list.count(result_list[j])
            result_list = result_list[j + 1:]
            break
        j += 1
    i += 1

print(f"Total price holders = {res}")
