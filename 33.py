
arr = [1, 2, 3, 2, 4, 1, 2, 5]

frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

for key, value in frequency.items():
    print(key, ":", value)
