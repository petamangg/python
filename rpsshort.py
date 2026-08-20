import random, sys

choices = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0

print("Basic Rock Paper Scissors game! Three rounds!")

for x in range(1, 4):
    computer_choice = random.choice(choices)
    user_choice = input("What do you pick? (rock, paper, scissor) [q to exit]: ").lower()

    if user_choice == "q":
        sys.exit()

    while user_choice not in choices:
        print("Invalid Choice! Please Choose again.")
        user_choice = input("What do you pick? (rock, paper, scissor) [q to exit]: ").lower()

        if user_choice == "q":
            sys.exit()

    print(f"The computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
        user_score += 1

    else:
        print("You lose!")
        computer_score += 1

    print(f"You: {user_score} | Computer: {computer_score}\n")

print("\nFinal Result:")
if user_score > computer_score:
    print("You won against the computer!")
elif computer_score > user_score:
    print("The computer won!")
else:
    print("It's a tie!")