# we can use sys.exit to exit a program early for example
# we also need to use import sys
import sys
check = input("Enter 'exit' to exit : ")
if check.lower() =="exit":
    sys.exit()
print(f"You typed {check}.")