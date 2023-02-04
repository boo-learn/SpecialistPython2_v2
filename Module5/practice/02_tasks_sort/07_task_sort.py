import random as r


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


n = 10
olimp_results = [r.randint(1, 10) for _ in range(n)]
sort_choice(olimp_results)
olimp_results = olimp_results[-1::-1]
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
