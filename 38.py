numbers = [0, 5, 0, 3, 8, 0, 2]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

result.extend([0] * (len(numbers) - len(result)))

print("Updated List:", result)