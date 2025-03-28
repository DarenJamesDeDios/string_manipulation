#center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function
text = "Hello"
width = 20
fillchar = " "
# Calculate the total padding required
total_padding = width - len(text)

# If the width is smaller than the text, just use the text as it is
if total_padding > 0:
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    centered_text = fillchar * left_padding + text + fillchar * right_padding
else:
    centered_text = text

print(centered_text)
