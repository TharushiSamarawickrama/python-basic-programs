# Basic Programs - Level 3: Patterns & Numbers

print("Level 3: Patterns & Numbers")
print("--------------------------------")

# 15. Pattern 1
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *

print("15. Pattern 1")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("--------------------------------")




# 16. Pattern 2
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("16. Pattern 2")

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("--------------------------------")




# 17. Pattern 3
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *

print("17. Pattern 3")

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("--------------------------------")




# 18. Count digits in a number

print("18. Count digits in a number")

number = int(input("Enter a number: "))
count = 0

# Use absolute value to handle negative numbers
number = abs(number)

if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count = count + 1

print("Number of digits:", count)

print("--------------------------------")




# 19. Reverse a number

print("19. Reverse a number")

number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)

print("--------------------------------")




# 20. Check if a number is a palindrome

print("20. Check if a number is a palindrome")

number = int(input("Enter a number: "))
original_number = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original_number == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")