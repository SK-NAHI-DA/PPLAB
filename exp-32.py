import re

string = input("Enter a string: ")

pattern = r'^([a-zA-Z]).*\1$'

if re.search(pattern, string):
    print("The given string starts and ends with the same character")
else:
    print("The string does NOT start and end with the same character")
