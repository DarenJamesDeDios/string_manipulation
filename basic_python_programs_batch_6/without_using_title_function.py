#title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
string = "How are you?"
words = string.split()  # Split the string into words
title_string = ""
for word in words:
    title_string += word.capitalize() + " " # Capitalize each word and add a space after it

print(title_string)