

"""Even or Odd
Write a function called even_or_odd that takes a single number as input.

Your task is to check whether the number is even or odd.

If the number is even (divisible by 2), return the string "even".

If the number is odd (not divisible by 2), return the string "odd".

You do not need to handle decimal numbers — only whole numbers will be passed in."""
def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd" 
"""Max of Two
Write a function called maximum that takes two numbers as input.

Your task is to return the larger of the two numbers.
If both numbers are the same, you can return either one."""
def maximum(a, b):
    if a > b:
        return a 
    elif b > a:
        return b
    else:
        return a

"""Repeat a Word
Write a function called repeat_word that takes two arguments:

A word (string)

A number (how many times to repeat the word)


Your task is to return a single string where the word is repeated that number of times with no spaces in between.

If the number is 0, return an empty string."""
def repeat_word(word, count):
    counted_word = word * count
    return counted_word
    if count == 0:
        return ""

# Sum List
"""Write a function called sum_list that takes a list of numbers as input and returns the total sum of all the numbers in the list.

If the list is empty, return 0."""
def sum_list(numbers):
    total = 0
    if numbers == []:
        return 0
    for number in numbers:
        total += number
    return total

"""Count the Letter 'a'
Write a function called count_a that takes a string as input.
Your task is to count how many times the lowercase letter 'a' appears in the string.

You do not need to check for uppercase 'A'. Only count lowercase 'a'."""
def count_a(text):
    counter = 0
    for letter in text:
        if letter == 'a':
            counter += 1
    return counter
    
""" Add Digits in a String
Write a function called sum_digits that takes a string made up of digits (like "12345").

Your task is to return the sum of all the digits in the string.

If the string is empty, return 0.

You may assume the string only contains numeric characters ('0' through '9').   """
    
def sum_digits(text):
    total = 0
    for char in text:
        number=int(char)
        total += number
    return total


"""
Count Evens
Write a function called count_evens that takes a list of numbers as input.

Your task is to count how many of the numbers in the list are even (divisible by 2), and return that count.

If the list is empty, return 0.
"""

def count_evens(numbers):
    count = 0
    if numbers is None:
        return 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

count_evens([1, 2, 3, 4, 5])        # Returns: 2
count_evens([2, 4, 6, 8])           # Returns: 4
count_evens([1, 3, 5, 7])           # Returns: 0
count_evens([])                     # Returns: 0
count_evens([0, 11, 22, 33])


"""Is It a Vowel?
Write a function called is_vowel that takes a single character as input.

Your task is to check if the character is a lowercase vowel ('a', 'e', 'i', 'o', or 'u').

Return True if it is, and False if it is not.

If the input is not a single character, you do not need to handle that — assume valid input."""

def is_vowel(letter):
    if letter in "aeiou":
        return True
    else:
        return False
is_vowel("a")       # Returns: True
is_vowel("e")       # Returns: True
is_vowel("b")       # Returns: False
is_vowel("A")       # Returns: False
is_vowel("u")       # Returns: True

"""Reverse String
Write a function called reverse_string that takes a string as input.

Your task is to return a new string that has the same characters in reverse order.

If the input string is empty, return an empty string."""
def reverse_string(text):
    reversed_text = text[::-1]
    return reversed_text
reverse_string("hello")        # Returns: "olleh"
reverse_string("apple")        # Returns: "elppa"
reverse_string("")             # Returns: ""
reverse_string("a")            # Returns: "a"
reverse_string("12345")        # Returns: "54321"


"""
Remove Vowels from a String
Write a function called remove_vowels that takes a string as input.

Your task is to return a new string with all lowercase vowels removed.

The vowels are: 'a', 'e', 'i', 'o', 'u'.

Only remove lowercase vowels. Keep everything else the same."""
def remove_vowels(text):
    removed_vowels = ''
    for letter in text:
        if letter not in 'aeiou':
           removed_vowels += letter
    return removed_vowels
remove_vowels("hello")         # Returns: "hll"
remove_vowels("apple pie")     # Returns: "ppl p"
remove_vowels("HELLO")         # Returns: "HELLO"
remove_vowels("aeiou")         # Returns: ""
remove_vowels("")              # Returns: ""

"""Replace Spaces with Hyphens
Write a function called replace_spaces that takes a string as input.

Your task is to return a new string where every space (" ") is replaced with a hyphen ("-").

Important:
Do not use the built-in .replace() method.

You must loop through the string and build a new one."""
def replace_spaces(text):
    new_string = ''
    for char in text:
        if char == " ":
            char = "-"
        new_string += char
    return new_string
replace_spaces("hello world")            # Returns: "hello-world"
replace_spaces("a b c")                  # Returns: "a-b-c"
replace_spaces("no_spaces_here")         # Returns: "no_spaces_here"
replace_spaces("  leading and trailing ")# Returns: "--leading-and-trailing-"
replace_spaces("")                       # Returns: ""

"""Temperature Converter
Develop a Python function named convert_temperature that converts a given temperature from Celsius to Fahrenheit or from Fahrenheit to Celsius based on the unit provided."""

"""Function Requirements:

Input:

temp (float): The temperature value that needs to be converted.

unit (str): A string representing the unit of the input temperature. The value should be either 'C' for Celsius or 'F' for Fahrenheit.

Output:

Returns the converted temperature as a float if the unit is valid.

Returns None if an invalid unit is provided, indicating the error.

Formulas:

To convert a temperature from Celsius to Fahrenheit:

F = (C * 9/5) + 32

To convert a temperature from Fahrenheit to Celsius:

C = (F - 32) * 5/9

Error Handling:

The function should be able to gracefully handle cases where the unit is neither 'C' nor 'F'. In such cases, the function should return None and not perform any conversion.

Examples:

Converting 20°C should return 68.0°F.

Converting 68°F should return 20.0°C."""
def convert_temperature(temp, unit):
    
    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit
    if unit == "F":
        celsius = (temp - 32) * 5/9 
        return celsius
    return None


"""Second Largest Number
Write a function called second_largest that takes a list of numbers as input.

Your task is to return the second largest number in the list.

You may assume:

The list has at least two different numbers

All numbers are integers

The list may or may not be sorted



Hint: Initialize your variables to negative infinity like this:

float('-inf')"""





def second_largest(numbers):
    first = float('-inf')
    second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
            
        elif number > second and number != first:
            second = number
    return second

second_largest([5, 1, 9, 3, 7])        # Returns: 7
second_largest([2, 4])                 # Returns: 2
second_largest([10, 10, 5, 8])         # Returns: 8
second_largest([1, 100, 99, 50])       # Returns: 99
second_largest([-5, -1, -3])           # Returns: -3

"""Is List Ascending?
Write a function called is_ascending that takes a list of numbers as input.

Your task is to return True if the list is in strict ascending order — meaning each number is less than the one after it.

If the list is empty or has only one item, return True."""

def is_ascending(numbers):
    if len(numbers) == 1:
        return True
    if None in numbers:
        return True
    acsend = 0
    for i in range(len(numbers)):
        if numbers[i] > acsend:
            acsend = numbers[i]
        else:
            return False
    return True
is_ascending([1, 2, 3, 4, 5])     # Returns: True
is_ascending([2, 2, 3])           # Returns: False
is_ascending([10, 9, 8])          # Returns: False
is_ascending([5])                 # Returns: True
is_ascending([])                  # Returns: True