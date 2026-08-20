#random adventure game cause im really bored 

import random
print("Welcome to my adventure game! Complete till the end!")
name = input("Whats youre name : ")
choice =input(f"Welcome {name}, What would you like to play?")
print("1) Aston valley" \
"2) Jungle")

if choice == "1":
    print("*You walk slowly through the valley and come across a strange man*")
    talk = input("Do you talk to him? [ 1) Yes , 2) No ] : ")
    if talk == "1":
        print("Where are you from?... says the man")
