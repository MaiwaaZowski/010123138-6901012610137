data = [1, 3, 3, 2, 1, 1, 4, 3, 3]

def find_mode(arr):
    frequency = {}
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    mode = max(frequency, key=frequency.get)
    return mode

result = find_mode(data)

print(f"List: {data}\nMode: {result}")

#6901012610137
#Lab07-4