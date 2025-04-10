# Beneath each comment write the code and print out the result to check it works

# '''LISTS'''

# Create a list and assign it to a variable
# names = ['aigerim', 'aikol', 'max']

# Find the length of the list
# names_len = len(names)
# Append an item to the list
# names.append("gulnara")

# Find the value of an item in the list a specific index
# max = names[2]
# print(max)
# # Set the value of an item at a specific index
# names[0] = "aika"

# Check whether an item is in the list
# def check_name(names):
#     if "max" in names:
#         return True
# # Sort the list
# print(sorted(names))
# Iterate over the list using range, printing out each element and the index
# for i in range(0, len(names)):
#     print(names[i])
# Iterate over the list without using range, printing out each element
# for name in names:
#     print(name)

# '''TUPLES'''

# Create a tuple and assign it to a variable
# colors = ('red', 'green', 'yellow')

# Find the length of the tuple
# color_len = len(colors)
# print(color_len)
#  Find the value of an item in the tuple a specific index
# item1 = colors[0]
# print(item1)
# Check whether an item is in the tuple
# def find_green(colors):
#     if "green" in colors:
#         return True
# print(find_green(('red', 'green', 'yellow')))
# Iterate over the tuple using range, printing out each element and the index
# def print_all_colors(colors):
#     for i in range(0, len(colors)):
#         print(colors[i])
# print_all_colors(('red', 'green', 'yellow'))

# Iterate over the tuple without using range, printing out each element
# def print_all_colors(colors):
#     for color in colors:
#         print(color)
# print_all_colors(('red', 'green', 'yellow'))

# '''STRINGS'''

# Create a string and assign it to a variable
# my_name = 'aigerim'
# Find the length of the string
# len_name = len(my_name)
# print(len_name)
# Find the value of an character in the string a specific index
# m = my_name[6]
# print(m)

# Check whether an item is in the string
# def find_r(my_name):
#     if "r" in my_name:
#         return True
# print(find_r("aigerim"))
# Concatenate (add) two strings together
# last = 'kalygulova'
# full_name = last + " " + my_name
# print(full_name)
# Create an f-string
# full_name = f"{my_name} {last}"
# print(full)
# Split a string using .split
# full_name = last + my_name
# print(full_name)
# splited = "aigerim kalygulova".split()
# print(splited) # -> ['aigerim', 'kalygulova']

# names = "aigerim aikol max"
# str(updated_last) = names.split()
# print(updated_last)

# Join a list of strings using .join
# names = ['aikol', 'aigerim', 'max']
# joined = ", ".join(names)
# print(joined)
# Iterate over the string using range, printing out each character and the index
# name = 'aigerim'
# for i in range(0, len(name)):
#     print(name[i], i)
# Iterate over the string without using range, printing out each character
# for char in name:
#     print(char)
# '''DICTIONARIES'''

# Create a dictionary and assign it to a variable
student = {
    'name': 'aigerim',
    'age': 31,
    'location': "Seattle",
    "marital_status": "married",
    "has_a_child": True
}

# Find the length of the dictionary
# len_student = len(student)
# print(len_student)

# # Add a new key/value pair
# student["sex"] = "female"
# print(student)
# # Replace value for a given key
# student['name'] = 'aika'
# print(student)
# Check whether a key is in the dictionary
# def check_key(student):
#     if "age" in student:
#         return True
# print(check_key(student))
# Iterate over keys, printing each key
# for key in student:
#     print(key)
# Iterate over over key/value pairs using .items(), printing each key and value
# for key, value in student.items():
#     print(key, value)
# # '''SETS'''

# # Create a set and assign it to a variable
# my_set = set({"aigerim", "aikol", "max"})
# print(my_set)

# # Find the length of the set
# len_set = len(my_set)
# print(len_set)
# # Add a new element
# my_set.add("gulnara")
# print(my_set)
# # Remove an element
# my_set.remove("gulnara")
# print(my_set)
# # Check whether a element is in the set
# def find_name(my_set):
#   if "max" in my_set:
#     return True
# find_name(my_set)
# # Iterate over elements, printing each one out
# for name in my_set:
#     print(name)
# '''NUMBERS'''

# Add / subtract / multiply 2 numbers
# a = 10
# b = 3
# add = a + b
# subtract = b - a
# multiply = a * b
# # Divide two numbers using normal (float) division
# divide = a / b
# print(divide)
# # Divide two numbers using integer division
# divide = a // b
# print(divide)
# # Find the modulo (remainder) of two numbers
# modulo = a % b
# print(modulo)
# # Check whether a number is even/odd
# if a % 2 == 0:
#     print("even")
# if b % 2 != 0:
#     print("odd")
# # Round a float down to an int
# num = round(45.87)
# print(num)
# # '''FUNCTIONS'''

# # Write a function that takes no arguments and call it
# def say_hello():
#     print("hello there")
# say_hello()

# # Write a function that takes one or more arguments and call it
# def happy_birthday(name):
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print(f"Happy birthday dear {name}")
#     print("Happy birthday to you")
# happy_birthday("Aigerim")
# Write a function that returns a value. Call the function and store the return value in a variable
# def add(num1, num2):
#     return num1+ num2
# print(add(2, 2))
# '''LOOPS'''

# # Write a while loop
# msg = input("Say magic word: ")

# while msg:
#     msg = input("Say magic word: ")
#     if msg == "max":
#         break
    
# # Write a for loop that loops a set number of times (e.g. 10 times)
# for i in range(0, 11):
#     print(i)

# '''CONDITIONALS'''

# Write an if/elif/else statement
# def find_name(name):
#     if name == "max":
#         print("this is my son")
#     elif name == "aikol":
#         print("this is my husband")
#     elif name == "aigerim":
#         print("this is me")
#     else:
#          print("I dont know you")
# find_name("asan")
    
# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=

# '''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second

# Iterate through the nested data structure using range

# Iterate through the nested data structure without using range 

# '''REMINDER'''

# You're doing great and you got this!