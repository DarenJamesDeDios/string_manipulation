#Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Ask for user input
inputed_fullname = input("Enter your fullname(make it in incorrect casing): ")

print(inputed_fullname.lower().replace(" ","_"))