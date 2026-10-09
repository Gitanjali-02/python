#1.print tables of all odd no from 1 to 10
#multiplication table
res=[]
for i in range(1, 11,2):
    for j in range(1, 11):
        res = i * j
        print(res,"")
    print()


#create a heterogenous list of numbers add names.split the list from highest number
my_list = [1, "Gita", "Mona", 8, 3, "Radha", 4, 5]

# Find the highest number
highest = max(x for x in my_list if isinstance(x, int))

# Split the list from the highest number
index = my_list.index(highest)

list1 = my_list[:index]
list2 = my_list[index:]

print("Highest number:", highest)
print("First list:", list1)
print("Second list:", list2)




#accept the name and check if its pallindrome 
n=int(input("enter the no:"))
rev=0
temp=n
while n>0:
    rev=rev*10+(n%10)
    n=n//10
if(rev==temp):
    print("pallindrome")
else:
    print("not pallindrome")



#print tha sum of digits
n=int(input("enter the no:"))
sum=0
temp=n
while n>0:
    sum=sum+(n%10)
    n=n//10
print("sum of digits:",sum)


#print the following pattern 
#   *
#   ##
#   ***
#   ####
#   *****

for i in range(1, 6):
    if i % 2 != 0:
        print("*" * i)
    else:
        print("#" * i)