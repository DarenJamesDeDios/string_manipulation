#index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
#initialized the strings and values
string = "She sells seashells by the seashore"
substring = "seashells"
# Loop through each character in the string
for i in range(len(string) - len(substring) + 1):
    # Check each character by comparing one by one
    match_found = True
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match_found = False
            break
    if match_found:
        print(f"The substring '{substring}' is found at index {i}.")
        break
else:
    print(f"The substring '{substring}' is not found.")
