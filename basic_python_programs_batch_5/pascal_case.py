#Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Ask for user input
inputed_fullname = input("Enter your fullname: ")

print(inputed_fullname.title().replace(" ",""))