# In this program we will be using the continue statement
while True:
    name = input("Who are you? : ")
    if name != "Joe":
        continue
    else:
        password = input("Hello, Joe. What is the password? (it is a fish) : ")
        if password == "swordfish":
            break

print("Access Granted")
        