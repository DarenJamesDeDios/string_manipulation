#swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function
string = "ReFrEsHiNg DrInKs"
alternate_string = []

for word in string:
    if word.isupper():
        alternate_string.append(word.lower())
    else:
        alternate_string.append(word.upper())
print(''.join(alternate_string))