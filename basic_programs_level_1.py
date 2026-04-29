# Basic Programs - Level 1: Warm-up


# 1. Print numbers from 1 to 100
print("1. Numbers from 1 to 100")
for i in range(1, 101):
    print(i)

print("--------------------------------")


# 2. Print numbers from 100 to 1
print("2. Numbers from 100 to 1")
for i in range(100, 0, -1):
    print(i)

print("--------------------------------")


# 3. Print even numbers from 1 to 100
print("3. Even numbers from 1 to 100")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

print("--------------------------------")


# 4. Print odd numbers from 1 to 100
print("4. Odd numbers from 1 to 100")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

print("--------------------------------")



# 5. Print multiplication table of a number
print("5. Multiplication Table")
number = int(input("Enter a number: "))

for i in range(1, 13):
    print(number, "x", i, "=", number * i)

print("--------------------------------")


# 6. Find sum of numbers from 1 to 100
print("6. Sum of numbers from 1 to 100")
total = 0

for i in range(1, 101):
    total = total + i

print("Sum is:", total)

print("--------------------------------")



# 7. Find sum of even numbers from 1 to 100
print("7. Sum of even numbers from 1 to 100")
even_total = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_total = even_total + i

print("Sum of even numbers is:", even_total)

print("--------------------------------")



# 8. Print numbers divisible by 3
print("8. Numbers divisible by 3")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)