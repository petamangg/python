#using list to make inputting easier. also if we use lists it reduces data redundancy in the program
catNames = [] #creating a list to store cat names
while True:
    name = input("Enter the name of cat " + str(len(catNames) + 1) + '(Or enter nothing to stop) : ')
    if name == "":
        break
    catNames = catNames + [name] # list concatenation
print("The cat names are : " )
for name in catNames:
    print(name)
print()