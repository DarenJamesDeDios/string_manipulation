#rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#initialized the strings and values
string = "hello world, hello universe"
substring = "hello"

#loop through the string starting from the end
for i in range(len(string) - len(substring), -1, -1):
    # Check if the substring matches starting at the current index
    match_found = True
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match_found = False
            break
    if match_found:
        print(f"The last occurrence of the substring '{substring}' is at index {i}.")
        break
else:
    print(f"The substring '{substring}' is not found.")
