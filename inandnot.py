# we will be using in and not operators
students = ['hari', 'ram', 'sita', 'gita']
name = input("Enter the student's name u want to find : ").lower()
if name not in students:
    print(f"{name} is not in this class")
else:
    print(f"{name} is in this class")
