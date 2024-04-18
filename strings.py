# string => string is the collection of characters(array of character)

# text = "Hello world"

# for i in text:
#     print(i)

# slicing

# print(text[0])
# print(text[2])

# accessing range of element
# print(text[0:5])
# print(text[6:])
# print(text[:8])

# negative indexing in python
# print(text[-3:-1])

# print(text[0:5:2])

# print(text[0::2])


# modifying string 

text = "we are learning python"

#converting into uppercase
upperText = text.upper()
print(upperText)

second_text = "THIS IS TEXT IN UPPERCASE"
#converting into lowercase
lowerText = second_text.lower()
print(lowerText)

greet = "Hello everyone in python class. we are learning python"
# to count the word present in the string we use count() method
count_python = greet.count("python")
print(count_python)

# to find the length of the string
print(len(greet))

# to replace the given character of the string with another character we use
# replace(character to be replace, character which replace it)

replace_greet = greet.replace("python","Django")
print(replace_greet)

# to remove the whitespace from the beginnig and end of the string
next_text = "  Hello world   "
print(next_text)
print(next_text.strip())


my_text = "we are learning python and django"
splitted_text = my_text.split("and")
print(splitted_text)