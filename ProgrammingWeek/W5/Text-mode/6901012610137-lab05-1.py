# a. find max, min, and average of an array
def find_max_min_avg(arr):
    max_val = arr[0]
    min_val = arr[0]
    total = 0
    i = 0
    while i < len(arr):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
        total = total + arr[i]
        i = i + 1
    avg = total / len(arr)
    return max_val, min_val, avg


# b. find index of max and min value
def find_max_min_index(arr):
    max_idx = 0
    min_idx = 0
    i = 1
    while i < len(arr):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i
        i = i + 1
    return max_idx, min_idx


# c. search for a value, return its index (-1 if not found)
def search_value(arr, target):
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i = i + 1
    return -1


# d. count elements greater than the average
def count_above_average(arr):
    total = 0
    i = 0
    while i < len(arr):
        total = total + arr[i]
        i = i + 1
    avg = total / len(arr)

    count = 0
    i = 0
    while i < len(arr):
        if arr[i] > avg:
            count = count + 1
        i = i + 1
    return count


# e. check whether array is increasing (sorted ascending)
def is_increasing(arr):
    i = 1
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            return False
        i = i + 1
    return True


# --- quick test ---
data = [3, 7, 2, 9, 4, 9, 1]

print(find_max_min_avg(data))       # (9, 1, 5.0)
print(find_max_min_index(data))     # (3, 6)
print(search_value(data, 4))        # 4
print(search_value(data, 100))      # -1
print(count_above_average(data))    # 2
print(is_increasing(data))          # False
print(is_increasing([1, 2, 2, 5]))  # True

#6901012610137
#Lab05-1