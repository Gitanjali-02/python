#empty list
my_list=[]
print(my_list)

#with items
fruits=["apple","banana","cherry"]
print(fruits)

#to access list elements use index
#positive no indicate from start negative no 

numbers=[10,20,30,40]
print(numbers[0])
print(numbers[-2])

colors=["red","blue"]
colors.append("green")
print("After insertion ",colors)

colors.insert(1,"yellow")
print("after insertion at 2nd position",colors)

last_color=colors.pop()
print(last_color)
print("after pop:",colors)

numbers=[1,2,3,4,5,7,8,9]
print("no of items:",len(numbers))

print("sum of all elements:",sum(numbers))

print("ascending order:",sorted(numbers))
print("decending oredr:",sorted(numbers ,reverse=True))