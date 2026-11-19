
arr = [12, 45, 23, 67, 34, 67]

unique = list(set(arr))
unique.sort()

if len(unique) >= 2:
    print("Second Largest:", unique[-2])
else:
    print("Second largest does not exist")
