#input principle time and rate to find out the principle
principle = float(input("Enter the Principle : "))
time = float(input("Enter the Time : "))
rate = float(input("Enter the Rate : "))
si = (principle * time * rate ) / 100
print(f"The Simple Interest is : {si}")