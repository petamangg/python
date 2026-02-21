#this is a python code to simulate a  stock
#this is not a real stock nor it uses any real time data its just a program meant for entertainment

import random
print("Welcome to the stock market... Choose a market to buy")
print("1) Apple" \
"2) Nvidia")
choice = input("Which stock would you like to buy : ").lower()
choices = ["nvidia","apple"]
chance = ["Tech Boom" , "Market Crash",]
currency = 10000

if choice == "1":
    print(f"You currently have {currency}$")
    money = input("How much money worth of stock do you wanna buy : ")
    currency -= money
    print(f"You have {currency}$ left ")
    chances = random.choice(chance)
    print(f"{choices} Happened!")
    currency *= 2 
    print(f"Youre new earnings are : {currency}")
    
    

