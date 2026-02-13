word=input("enter word")
vowels={'a','e','i','o','u',
        'A','E','I','O','U'}
found='false'
for ch in word:
    if ch in vowels:
        found='true'
        break
    if found:
        print("word in vowels")
    else:
        print("word not in vowels")
