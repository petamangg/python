import random

choices = ["rock","paper","scissors"]
print("Welcome to my Rock Paper Scissors game.")

user_score = 0
computer_score = 0

while True:
    print("Press q to quit!")
    user_choice = input("Enter your choice (Rock, Paper, Scissors): ").lower()

    if user_choice == "q":
        print(f"Your score is: {user_score}   Computer score is: {computer_score}")
        break

    if user_choice not in choices:
        print("Invalid Input! Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")

    if (user_choice == "rock" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "rock"):
        print("You lost!")
        computer_score += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You won!")
        user_score += 1
#this is a simple game made my peter tamang!

