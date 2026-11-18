import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(ch.isupper() for ch in password):
        score += 1

    if any(ch.islower() for ch in password):
        score += 1

    if any(ch.isdigit() for ch in password):
        score += 1

    if any(ch in string.punctuation for ch in password):
        score += 1

    if score <= 2:
        return "Weak Password"
    elif score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"


password = input("Enter your password: ")
print(check_password(password))