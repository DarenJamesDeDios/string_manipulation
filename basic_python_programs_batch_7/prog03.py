#upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
#initialized the strings and values
string = "Daren James De Dios"
result = ""
#a block of code that checks lowercase letters and converts them to uppercase letters
for letter in string:
    if 'a'<= letter <= 'z' :
        result += chr(ord(letter) -32) 
    else:
        result += letter
#print the result
print(result)
