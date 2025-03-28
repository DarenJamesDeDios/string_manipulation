#lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
#initialization
string = "Daren James De Dios"
result = ""

for letter in string:
    if 'A' <= letter <= 'Z': 
        result += chr(ord(letter) + 32) 
    else:
        result += letter

print(result)
