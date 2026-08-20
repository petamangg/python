#basic elif statements
name = input("Are you Alice? (yes or no) : ").lower()
age = int(input("Whats youre age? : "))
if name == "yes":
    print("Hi , Alice ")        

else:
    if age < 12:
        print("You are not Alice, kiddo")
    elif age > 1000:
        print("Unlike you, Alice is not an undead, immortal vampire")
    elif age > 100:
        print("You are not Alice, grannie")
    else:
        print("You are not Alice") 