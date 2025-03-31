#startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
#initialized the strings and values
string = "DeDios"
startswith = "De"
#a block of code that checks if the string starts with the specified prefix and print True or False
if string[:len(startswith)] == startswith:
    print(f"The string '{string}' ends with '{startswith}'.")
else:
    print(f"The string '{string}' does not start with '{startswith}'.")