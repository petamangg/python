#This is a simple rock paper scissors game 
#import 
#keep track of variables
#display what the player choses
#display what the computer chooses
#display the score (tie lose win)

import random , sys

choices = ["rock" , "paper" , "scissor" , "q"]
user_score = 0 
computer_score = 0

print("Basic Rock Paper Scissors game! Three rounds!")
for x in range(1,4):
    computer_choice = random.choice(choices)
    user_choice = input("What do you pick? (rock , paper , scissor) [q to exit] : ").lower()
    while user_choice not in choices:
        print("Invalid Choice! Please Choose again.")
        user_choice = input("What do you pick? (rock , paper , scissor) [q to exit] : ").lower()
    if user_choice == "q":
        sys.exit()
    if user_choice == computer_choice:
        print(f"The computer chose : {computer_choice}")
        print("Its a tie.")
        print()
    elif user_choice == "rock" and computer_choice == "paper":
        print(f"The computer chose : {computer_choice}")
        print("You lose! Paper covers rock")
        computer_score += 1
        print(f"Computer Score is : {computer_score}")
        print()
    elif user_choice == "paper" and computer_choice =="rock":
        print(f"The computer chose : {computer_choice}")
        print("You win! Paper covers rock")
        user_score += 1
        print(f"Youre score is : {user_score}")
        print()
    elif user_choice == "rock" and computer_choice == "scissor":
        print(f"The computer chose : {computer_choice}")
        print("You win! Rock breaks scissor")
        user_score += 1
        print(f"Youre score is : {user_score}")
        print()
    elif user_choice == "scissor" and computer_choice == "rock":
        print(f"The computer chose : {computer_choice}")
        print("You lose! Rock Breaks Scissor")
        computer_score += 1
        print(f"Computer Score is : {computer_score}")
        print()
    elif user_choice =="paper" and computer_choice == "scissor":
        print(f"The computer chose : {computer_choice}")
        print("You lose! Scissor cuts paper")
        computer_score += 1 
        print(f"Computer Score is : {computer_score}")
        print() 
    elif  user_choice == "scissor" and computer_choice =="paper":
        print(f"The computer chose : {computer_choice}")
        print("You win! Scissor cuts paper")
        user_score += 1
        print(f"Youre score is : {user_score}")
    else:
        print()
print()
print()
        
if computer_score > user_score:
    print("The computer won!")
elif user_score > computer_score:
    print("You won against the computer!")
else:
    print("Its a tie!")
print()
print()


        
    

  

  

