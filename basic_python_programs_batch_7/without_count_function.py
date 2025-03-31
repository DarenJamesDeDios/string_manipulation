#count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
#initialized the strings and values
word = 'woodchuck'
String = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
List = []
#used for-loop to split the strings into words and put them into an index
for i in String.split():
    List.append(i)
#another for-loop to check the string for the same word and adds them into count"
count = 0

for i in List:
    if i == word:
        count += 1

    else:
        continue

print(count)
