import random

def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num

def selection_sort(num):
    n = len(num)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if num[j] < num[min_idx]:
                min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]
    return num

def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[0]
    left = []
    right = []
    for i in range(1, len(num)):
        if num[i] < pivot:
            left.append(num[i])
        else:
            right.append(num[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    return [random.randint(at, to) for i in range(size)]


arr1 = gen_list(10)
print("Unsorted list 1:", arr1)
sorted_arr1 = bubble_sort(arr1)
print("Bubble Sorted list 1:", sorted_arr1)
sorted_arr1 = selection_sort(arr1)
print("Selection Sorted list 1:", sorted_arr1)
sorted_arr1 = quick_sort(arr1)
print("Quick Sorted list 1:", sorted_arr1)

