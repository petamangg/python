#another elif program
name = input("Is youre name Alice ? (yes or no) : ").lower()
if name == "yes":
    print("Hi, Alice.")
else:
    age =input("Whats youre age? : ")
    if int(age) < 12 :
        print("You are not Alice, kiddo")
    else: 
        print("You are neither Alice nor a little kid.")


