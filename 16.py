
num = int(input("Enter a number: "))

temp = num
total = 0
power = len(str(num))

while temp > 0:
    digit = temp % 10
    total = total + digit ** power
    temp = temp // 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
