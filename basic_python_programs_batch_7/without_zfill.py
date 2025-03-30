#zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
#planning to use f-strings instead
inputed_number = (input("Enter a number from 0-1000: ")) #user input for more interaction 

print(f"{inputed_number:06}") #f-string for adding zeros

