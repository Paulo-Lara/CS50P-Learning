#Camel case = When there is a capitalized letter, an "_" must be on snake_case before that capitalized letter
#This is why in extensions.py i used for loop, I knew I was gonna use it
camel_case = input("camelCase: ")

mayus = 0
for letra in camel_case:
    if letra.isupper() == True:
        mayus = letra.lower()
        print("_" + mayus, end="")
    else:
        print(letra, end="")