#rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
#initialized the strings and values
string = "hello world, hello universe"
substring = "hello"

#loop through the string starting from the end
for i in range(len(string) - len(substring), -1, -1):

