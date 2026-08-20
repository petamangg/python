#program that uses match

name = input("Enter your name : ").lower()


match name:
    case "Peter":
        print("You are hero")
    case "Puri":
        print("You are Kuri")
    case "Peter1":
        print("Grffin")
    case _:
        print("Bruh")