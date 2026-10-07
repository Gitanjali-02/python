#sample string
text= " Welcome to IMCC!  "

#strip spaces from both ends
print("REmove spaces:",text.strip())

#
print("Lower case:",text.lower())

print("Upper case:",text.upper())

text=text.strip()
print("Captilize first letter:",text.capitalize())

#Title case(capitalize each word)
print(text.title())

# count occurrence of a substring
print(" Letter c occurs ",text.count("c"),"times in text")

#find the position of a substring(-1 if not found)
print("position of IMCC is:",text.find("IMCC"))

#replace a substring
print(text.replace("IMCC","Python magic"))

#check if string starts or ends with certain substring
print(text.startswith(" We"))
print(text.endswith("! " ))

print(text.split())
words=["python","is","good"]
print()

