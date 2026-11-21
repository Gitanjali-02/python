arr = [0, 10, 0, 20, 30, 0, 40]

result = [x for x in arr if x != 0]
zeros = arr.count(0)

result.extend([0] * zeros)

print(result)