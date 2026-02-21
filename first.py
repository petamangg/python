#trying to make a calculator.
print("Welcome to my Calculator!")

num1 =float(input("Enter the first number : "))
num2 =float(input("Enter the second number : "))
operation = (input("Enter Operation ( + , - , / , * ) : "))

if operation == "+":
    result= num1 + num2 
elif operation == "-":
    result = num1 - num2 
elif operation == "/":
    result = num1 / num2
elif operation == "*":
    if num2 != 0:
        result= num1 * num2

    else : "Error cant divide by zero"

else: result="Invalid Operation!"

print("Result : ",result)
