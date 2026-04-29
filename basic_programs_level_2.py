# Basic Programs - Level 2: Conditions

print("Level 2: Conditions")
print("--------------------------------")


# 9. Check if a number is positive, negative, or zero
print("9. Check if a number is positive, negative, or zero")

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("--------------------------------")



# 10. Check if a number is even or odd
print("10. Check if a number is even or odd")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("--------------------------------")



# 11. Find the largest of two numbers
print("11. Find the largest of two numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("The largest number is:", num1)
elif num2 > num1:
    print("The largest number is:", num2)
else:
    print("Both numbers are equal.")

print("--------------------------------")



# 12. Find the largest of three numbers
print("12. Find the largest of three numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

print("--------------------------------")



# 13. Check if a number is divisible by both 3 and 5
print("13. Check if a number is divisible by both 3 and 5")

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

print("--------------------------------")



# 14. Create a grade system
print("14. Grade System")

marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Grade: A")
elif marks >= 65:
    print("Grade: B")
elif marks >= 55:
    print("Grade: C")
elif marks >= 35:
    print("Grade: S")
else:
    print("Grade: F")