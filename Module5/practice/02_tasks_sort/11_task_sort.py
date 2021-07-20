lst = [1, 2, 3, 1, 3]

for i, el_target in enumerate(lst):
    for j, el_equal in enumerate(lst, start=i+1):
        if len(lst) > j > i and el_target == el_equal:
            print(f'{j}: {el_equal}')
