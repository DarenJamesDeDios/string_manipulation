#rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
#initialized the strings and values
text_string = "Using python language******"
index_string = len(text_string) - 1
#a block of code that checks the trailing spaces of the string
while index_string >= 0 and text_string[index_string] == '*':
    index_string -= 1
#printting the desired output
myrstripv = text_string[:index_string + 1] # Slice the string up to the last non-space character
print(myrstripv)