# welcome to my gambling game
# this is game where u can have money and u gamble with it
import random
print("Welcome to my gambling game! This game uses in game currency to gamble!")
user_money = 10000  # default money that the user gets is 10k dollars
print(f"You have {user_money}$")  # fixed string formatting
print("")

print("1) Dice game!")
print("2) Coin Flip game!")
user_choice = input("Which game do you wanna play? : ")

print("")

while True:
    if user_choice == "1":  # input is a string, so compare with "1"
        money = int(input("How much money would you like to put in : "))
        user_money -= money
        print("Welcome to my dice game ! Press Q to quit")
        choices = [1, 2, 3, 4, 5, 6]  # fixed range for dice

        choice = input("Choose a random number from 1 to 6 : ")  # choosing a number
        comp = random.choice(choices)
        print(f"The dice rolled: {comp}")


        if choice.lower() == "q":  # fixed missing parentheses
            print(f"You have {user_money}$")
            break  # to quit
        # break would only work inside a loop

        else:
            choice = int(choice)  # convert input to integer for comparison
            if choice == comp:
                print("You won! ")
                user_money += 2* money
                print(f"You have {user_money}$ left")
            elif choice < comp:
                print("You lost! Too low!")
                print(f"You have {user_money}$ left")
            else:
                print("You lost! Too high!")
                print(f"You have {user_money}$ left")

    elif(user_choice == "3"):
       
        print("Welcome to my coin flip game!")
        choice = str(input("Enter which side the coin will flip(Head , Tails) : ").lower())
        money = int(input("Enter the ammount of money you wanna put in : "))
        choices = ["head", "tails"]
        choices2 = random.choice(choices)
        print(f"The coin flipped {choices2}")
        if(choices2 == choice):
            print("You won!")
            user_money += money * 2
            print(f"You have {user_money}$")
        else:
            print("You lost!")
            user_money -= money
            print(f"You have {user_money}$ left")
# still left to make a lot of changes and stuff like that.. i will try to do it in javascript too

    else:
        print("This game is still on construction")



