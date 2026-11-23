numbers = [16, 17, 4, 3, 5, 2]
leaders = []

for i in range(len(numbers)):
    if all(numbers[i] > num for num in numbers[i+1:]):
        leaders.append(numbers[i])

print("Leaders:", leaders)