#capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
string = "Hello, EvEryONe"

capitalized_string = string[0].upper() + string[1:].lower()
 
print(capitalized_string)