# removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function
#initialized the strings and values
string =  "Daren James De Dios"
suffix_remove = "ios"
#a block of code that checks if the string has the suffix in the end of the string
if string.endswith(suffix_remove):
    result = string[:-len(suffix_remove)] #check if the strings ends with the specified suffix
else:
    result = string
#printting the result
print(result)