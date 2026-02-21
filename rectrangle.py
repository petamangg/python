#making a rectrangle in a terminal

rows = int(input("How many rows would you like : "))
columns = int(input("How many columns would you like : "))
symbol = input("Enter a symbol : ")



for x in range(rows):
    for y in range(columns):
        print(symbol , end="")
    print()
    