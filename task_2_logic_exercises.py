# Task 2: Logic Exercises

print("Task 2: Logic Exercises")
print("--------------------------------")



# 1. FizzBuzz from 1 to 100

print("1. FizzBuzz from 1 to 100")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("--------------------------------")




# 2. Find largest number in an array

print("2. Find largest number in an array")

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




# 3. Count vowels in a string

print("3. Count vowels in a string")

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count = vowel_count + 1

print("Number of vowels:", vowel_count)

print("--------------------------------")




# 4. Palindrome checker

print("4. Palindrome checker")

text = input("Enter a word or text: ")

clean_text = text.lower()
reversed_text = clean_text[::-1]

if clean_text == reversed_text:
    print("This is a palindrome.")
else:
    print("This is not a palindrome.")