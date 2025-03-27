#lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
#initialization
text_string = "    I am a programmer"
index_string = 0
#need to make a block of code that remove spaces but stop when the it is a letter
while index_string < len(text_string) and text_string[index_string] == ' ':
    index_string += 1
    
mylstripv = text_string[index_string:]
print(mylstripv)