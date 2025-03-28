#ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
string = "James"
width = 10
fill_char = " "

padding_needed = width - len(string)

if padding_needed > 0:
    string = string + (fill_char * padding_needed)

print(string, "Reid") 


