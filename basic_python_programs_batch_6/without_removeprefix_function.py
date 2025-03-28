#removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function
string =  "Daren James De Dios"
prefix_remove = "Dar"

if string.startswith(prefix_remove):
    result = string[len(prefix_remove):]
else:
    result = string
