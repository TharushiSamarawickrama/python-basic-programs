# Basic Programs - Level 5: Logic

print("Level 5: Logic")
print("--------------------------------")



# 26. Find factorial of a number

print("26. Find factorial of a number")

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is: 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "is:", factorial)

print("--------------------------------")




# 27. Check if a number is prime

print("27. Check if a number is prime")

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

print("--------------------------------")




# 28. Print Fibonacci numbers

print("28. Print Fibonacci numbers")

terms = int(input("Enter number of terms: "))

first = 0
second = 1

print("Fibonacci series:")

for i in range(terms):
    print(first)
    next_number = first + second
    first = second
    second = next_number

print("--------------------------------")




# 29. Find largest number in an array entered by user

print("29. Find largest number in an array")

numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Numbers:", numbers)
print("Largest number is:", largest)

print("--------------------------------")




# 30. Find smallest number in an array entered by user

print("30. Find smallest number in an array")

numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Numbers:", numbers)
print("Smallest number is:", smallest)