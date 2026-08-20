import random

print("Welcome to Hand Cricket!")
print("Enter 67 anytime to quit.")
print("You are batting first.\n")

user_score = 0
computer_score = 0
choices = [1,2,3,4,5,6]

# USER BATTING
while True:
    choice1 = int(input("Choose a number (1–6): "))

    if choice1 == 67:
        print("Game quit!")
        exit()

    if choice1 not in choices:
        print("Invalid input!")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if choice1 == computer_choice:
        print("You're OUT!")
        break
    else:
        user_score += choice1
        print("Your score:", user_score)

print("\nComputer needs", user_score + 1, "runs to win.\n")

# COMPUTER BATTING
while computer_score <= user_score:
    choice2 = int(input("Bowl a number (1–6): "))

    if choice2 == 67:
        print("Game quit!")
        exit()

    if choice2 not in choices:
        print("Invalid input!")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if choice2 == computer_choice:
        print("Computer is OUT!")
        break
    else:
        computer_score += computer_choice
        print("Computer score:", computer_score)

# RESULT
print("\nFinal Scores:")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("🎉 You Win!")
elif user_score < computer_score:
    print("💀 You Lose!")
else:
    print("🤝 Tie! Super Over!")
