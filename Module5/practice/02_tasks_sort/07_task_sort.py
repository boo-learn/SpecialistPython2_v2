import random as r
n = 10
olimp_results = [r.randint(1, 10) for _ in range(n)]
olimp_results.sort(reverse=True)
print(olimp_results)
qty_win = 1
st_res = olimp_results[0]
j = 1
for i in range(1, n):
    if olimp_results[i] == st_res:
        qty_win += 1
    elif olimp_results[i] != st_res:
        j += 1
        if j > 3:
            break
        qty_win += 1
        st_res = olimp_results[i]

print(qty_win)
