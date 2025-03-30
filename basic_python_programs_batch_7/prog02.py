# removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function
string =  "Daren James De Dios"
suffix_remove = "ios"

if string.endswith(suffix_remove):
    result = string[:-len(suffix_remove)]
else:
    result = string

print(result)