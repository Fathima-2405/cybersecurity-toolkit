import re

password = input("Enter your password: ")

strength = "Weak"

if len(password) >= 8:
    if re.search("[A-Z]", password) and re.search("[0-9]", password):
        strength = "Strong"
    else:
        strength = "Medium"

print("Password Strength:", strength)
