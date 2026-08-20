import random
print("Welcome to my number guessing game!")

numtoguess = random.randint(1,10)
choice =int(input("Guess the number from 1 to 10 : "))

while choice != numtoguess:
    if choice < numtoguess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    choice =int(input("Guess again : "))

print("You gussed the correct number! You won!!")
