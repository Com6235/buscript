print("Calculator")

# Get user input and validate it
num1 = input("Enter the first number: ")
while not num1.isdigit():
    num1 = input("Invalid input! Please enter a number: ")
num1 = float(num1)

num2 = input("Enter the second number: ")
while not num2.isdigit():
    num2 = input("Invalid input! Please enter a number: ")
num2 = float(num2)

sign = input("What operation would you like to do?\n1) Add (+)\n2) Subtract (-)\n3) Multiply (*)\n4) Divide (/)\nPlease enter your choice: ")
while sign not in ["1", "2", "3", "4"]:
    sign = input("Invalid input! Please enter a valid choice: ")

# Perform the selected operation and print the result
if sign == "1":
    result = num1 + num2
elif sign == "2":
    result = num1 - num2
elif sign == "3":
    result = num1 * num2
elif sign == "4":
    result = num1 / num2

print("Result: " + str(result))
