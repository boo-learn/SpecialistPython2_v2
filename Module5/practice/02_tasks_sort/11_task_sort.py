lst = [1, 2, 3, 1, 3]

for i, el_target in enumerate(lst):
    res_str = f'{lst[i]}'
    was_found = False
    for j, el_equal in enumerate(lst, start=i+1):
        if len(lst) > j > i and el_target == el_equal:
            res_str += f' {lst[j]}'
            was_found = True
    if was_found:
        print(res_str)
