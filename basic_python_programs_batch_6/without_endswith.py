#endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
string = "DeDios"
suffix = "ios"

if string[-len(suffix):] == suffix:
    print(f"The string '{string}' ends with '{suffix}'.")
else:
    print(f"The string '{string}' does not end with '{suffix}'.")