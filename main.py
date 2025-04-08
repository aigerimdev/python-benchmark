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
for key, value in student.items():
    print(key, value)
# '''SETS'''

# Create a set and assign it to a variable

# Find the length of the set

# Add a new element

# Remove an element

# Check whether a element is in the set

# Iterate over elements, printing each one out

# '''NUMBERS'''

# Add / subtract / multiply 2 numbers

# Divide two numbers using normal (float) division

# Divide two numbers using integer division

# Find the modulo (remainder) of two numbers

# Check whether a number is even/odd

# Round a float down to an int


# '''FUNCTIONS'''

# Write a function that takes no arguments and call it

# Write a function that takes one or more arguments and call it

# Write a function that returns a value. Call the function and store the return value in a variable

# '''LOOPS'''

# Write a while loop

# Write a for loop that loops a set number of times (e.g. 10 times)

# '''CONDITIONALS'''

# Write an if/elif/else statement

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