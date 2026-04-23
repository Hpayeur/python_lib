# Variables
age = 50
# price = 19.95
# first_name = "john"
# is_online = False
print(age)

# Receiving Input
name = input("Enter Your Name")
print("Hello " + name)

# Type Conversion
first = float(input("First"))
second = input("Second")
sum = float(first) + float(second)
print("Sum: " + str(sum))

# Strings
# Examples: upper, lower, find, and replace
course = 'Python For Beginners'
print('Python' in course)

# Arithmetic Operators
# Examples: +, -, *, /, //, %, **, and +=
x = (10 + 5) * 15
print(x)

# Comparison Operators
# Examples: >, >=, <, <=, ==, and !=
x = 3 > 2
print(x)

# Logical Operators
# Examples: And = Both, Or = One at Least, Not
price = 5
print (price > 10 and price < 30)
print(price > 10 or price < 30)
print (not price > 10)

# If Statements
temperature = 90
if temperature > 50:
    print("It's A Hot Day")
    print("Please Drink Lot's of Water")
elif temperature > 20: # (20, 30]
    print("It's a nice day ")
elif temperature < 20: # (10, 20]
    print("It's a bit cold")
else:
    print (" It's cold")
    print("Done")

# Exercise
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# While Loops
i = 1
while i <= 10:
    print (i * '*')
    i = i + 1
# Lists
names = ["John", "Lio", "Mario", "Anna", "Bryan"]
names[0] = "Jessie"
print(names[0:3])
print(names)

# List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove (3)
print(numbers)
numbers.clear()
print(numbers)
print(1 in numbers)
print(len(numbers))

# For Loops
numbers = [6, 7, 8]
for item in numbers:
    print(item)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
# The Range() Function
for number in range(5):
    print(number)
# Tuples
# Examples: count, and index
numbers = (1, 2, 3, 3)
numbers.count(3)