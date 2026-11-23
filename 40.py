expression = "{[()]}"
stack = []

pairs = {')': '(', '}': '{', ']': '['}

for char in expression:
    if char in "({[":
        stack.append(char)

    elif char in ")}]":
        if not stack or stack.pop() != pairs[char]:
            print("Not Balanced")
            break
else:
    print("Balanced" if not stack else "Not Balanced")