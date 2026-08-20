#This is a number guessing game
import random
secret = random.randint(1,20)
print("Im thinking of a number from 1 to 20")

# ask the player to guess 6 times 
for guessesTaken in range(1,7):
    guess = int(input("Take a guess : "))

    if guess < secret:
        print("Youre guess is low")
    elif guess > secret:
        print("Youre guess is high")
    else:
        break
if guess == secret:
    print(f"Congratulations! You guessed the correct number in {guessesTaken} times")
else:
    print(f"Nope! I was thinking of the number {secret}")

    
