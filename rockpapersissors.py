import random

print("Play Rock Paper Scissors!!")

choices = ["rock" , "paper" , "scissors"]  # these are the choices 

user_score = 0
computer_score = 0  # computer and user score 

while True:
    print(" Press q to exit")
    choice = input("Choose one : (Rock , Paper , Scissors) : ").lower() # the user chooses a choice from here

    if choice =="q":
        print(f"Game Over")
        print(f"Your score : {user_score} Computer score : {computer_score}")
        break

    if choice not in choices:
        print("Invalid Choice! Try again!")
        continue
    computer = random.choice(choices)
    print(f"The computer chose : {computer}")
    if choice == computer:
        print("Its a tie! ")
    elif(choice == "rock" and computer == "scissors") or \
        (choice =="paper" and computer == "rock") or \
        (choice == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else :
        print("You lose!")
        computer_score+= 1
    


