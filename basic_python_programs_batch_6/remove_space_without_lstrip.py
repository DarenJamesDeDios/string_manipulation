#lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
inputed_statement = input("Enter words with spaces in the beginning: ")

print(inputed_statement.replace(" ","").replace(""," "))