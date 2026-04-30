# Basic Programs - Level 4: Strings

print("Level 4: Strings")
print("--------------------------------")



# 21. Reverse a string

print("21. Reverse a string")

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)

print("--------------------------------")




# 22. Count vowels in a string

print("22. Count vowels in a string")

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count = count + 1

print("Number of vowels:", count)

print("--------------------------------")




# 23. Count consonants in a string

print("23. Count consonants in a string")

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count = count + 1

print("Number of consonants:", count)

print("--------------------------------")




# 24. Convert string to uppercase

print("24. Convert string to uppercase")

text = input("Enter a string: ")

uppercase_text = text.upper()

print("Uppercase string:", uppercase_text)

print("--------------------------------")




# 25. Check if string is a palindrome

print("25. Check if string is a palindrome")

text = input("Enter a string: ")

# Convert to lowercase to avoid case sensitivity
clean_text = text.lower()

reversed_text = clean_text[::-1]

if clean_text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")