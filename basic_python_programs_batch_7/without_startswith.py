#startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#initialized the strings and values
string = "De Dios"
startswith = "D"
#a block of code that checks if the string starts with the specified prefix
if string[len(startswith):] == startswith:
    print(f"The string '{string}' ends with '{startswith}'.")
else:
    print(f"The string '{string}' does not end with '{startswith}'.")