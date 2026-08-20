#the hand cricket game with some good interacations 
import random
import time 

print("Welcome to the Cricket game using Numbers!")
print("")
print("Enter 67 to quit game.")
print("You are batting first.")
user_score = 0
computer_score = 0
while True:
    choice1 = int(input("Choose a number from (1 to 6)  : "))
    choices = [1,2,3,4,5,6]
    
    if choice1 == 67:
        print("Game over!")
        print(f"Youre score : {user_score}")
        break
    
    if choice1 not in choices:
        print("Invalid input please try again")
        continue
        
    computer_choice = random.choice(choices)
    
    if computer_choice != choice1:
        user_score += choice1
    
    else:
        print(f"The computer is gonna try to get more than {user_score} runs ")
        print("Its computer's turn now.")
        choice2 = int(input("Enter a number from (1 to 6 ). : "))
        if choice2 != computer_choice:
            computer_score += choice2
        else:
            print(f"You got {user_score} runs and computer got {computer_score} runs.")
            if user_score > computer_score:
                print("Congratulations! You have won!")
            elif user_score < computer_score:
                print("Too bad! You lost!")
            else:
                print("Tie! Its superover!")
                break
            

        

    
    



