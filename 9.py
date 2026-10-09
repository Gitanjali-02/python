
# 1. Print sum of first 10 even numbers
total = 0
for i in range(2, 21, 2):
    total += i
print("Sum =", total)


# 2. Accept s and n. Print squares of first n numbers starting from s
s = int(input("Enter starting number: "))
n = int(input("Enter n: "))
for i in range(s, s + n):
    print(i * i)


# 3. Reverse the accepted string
s1 = input("Enter a string: ")
print(s1[::-1])


# 4. Accept sentence and count vowels
s = input("Enter a sentence: ")
count = 0
for ch in s.lower():
    if ch in "aeiou":
        count += 1
print("Number of vowels =", count)


# 5. Remove duplicates from list
l1 = [1, 2, 3, 2, 4, 1, 5]
l2 = list(dict.fromkeys(l1))
print(l2)


# 6. Reverse the list
l1 = [1, 2, 3, 4, 5]
print(l1[::-1])

