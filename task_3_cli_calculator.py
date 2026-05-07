# Task 3: Mini Project - CLI Calculator

print("Task 3: CLI Calculator")
print("--------------------------------")



# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Get operation from the user
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print("Result:", result)

elif operation == "-":
    result = num1 - num2
    print("Result:", result)

elif operation == "*":
    result = num1 * num2
    print("Result:", result)

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please enter +, -, *, or /.")

print("--------------------------------")