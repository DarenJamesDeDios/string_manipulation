# islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
#initialized the strings and values
string = input("Enter a statement/word: ")
lowercase_letters = 0
#a block of code that checks if all letters are lowercase
for letter in string:
    if letter.isupper():
        continue
    else:
        lowercase_letters += 1
#print if True or False
if len(string) == lowercase_letters:
    print("All letters are lowercase")
else:
    print("Not all letters are lowercase")