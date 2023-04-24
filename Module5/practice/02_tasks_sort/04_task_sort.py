def sort_choice(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if abs(arr[j]) > abs(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

sorted_numbers = sorted(numbers, key=abs, reverse=True)

sum_of_largest = sum(sorted_numbers[:5])

rounded_sum = round(sum_of_largest, 2)

print(rounded_sum)
