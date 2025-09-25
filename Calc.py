# Basic Calculator Program

# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter operation (+, -, *, /): ")

# Addition
if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)

# Subtraction
if operation == "-":
    print(num1, "-", num2, "=", num1 - num2)

# Multiplication
if operation == "*":
    print(num1, "*", num2, "=", num1 * num2)

# Division
if operation == "/":
    print(num1, "/", num2, "=", num1 / num2)
