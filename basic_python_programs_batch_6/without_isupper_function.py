#isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
string = input("Enter a statement/word: ")
uppercase_letters = 0
for letter in string:
    if letter.islower():
        continue
    else:
        uppercase_letters += 1
if len(string) == uppercase_letters:
    print("All letters are uppercase")
else:
    print("Not all letters are uppercase")