# Coding Exercise 8 - Extracting capitals

# Write a program to print out the capital letters in a string.

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUWVXYZ":
        print(char, end='')
