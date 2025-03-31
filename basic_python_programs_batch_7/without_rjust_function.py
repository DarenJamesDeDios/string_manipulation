#rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
#initialized the strings and values

string = "Lustre"
width = 10
fill_char = " "
#a block of code that adds space at the beginning of the string
padding_needed = width - len(string)

if padding_needed > 0:
    string = (fill_char * padding_needed) + string

print("Nadine", string) 
