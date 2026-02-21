import string

print("Password Strength Checker")

password = input("Enter your password: ")

passnum = len(password)

# special characters like !@#$%^&*() etc.
special_characters = string.punctuation
if passnum > 10 and any(char in special_characters for char in password):
    print("Your password is strong!")
else:
    print("Your password is weak!")

