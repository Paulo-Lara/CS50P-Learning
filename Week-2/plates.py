"""
No puede tener más de 6 carácteres (len)
len[0] y [1] tienen que ser letras
Si hay un numero en algun punto, la siguiente letra no puede ser una letra (ciclo for)
El primer numero no puede ser 0
Todo tiene que estar junto (función .strip ), no puede haber carácteres especiales ni nada
todo tiene que ser con letra o numeros, si algo no es, mal
Si algo de lo anterior es incorrecto, devolver falso, y por ende devolver Invalid
Si todo lo anterior es correcto, devolver Valid
...
...
Use loop for to go through each character on the plate input and analize what type
of character ir is, if it is a number, add it to a list that is just made up from numbers,
if it is a letter, move it to another list that is made up by just letters, that's how we identify
if the current character is a letter or a number, and therefore we can apply these rules
(for example, if on the number list there is a letter, it is and INMEDIATE invalid)
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) < 2 or len(plate) >= 7 or plate.isalnum() == False:
            return False
    if plate[0].isnumeric() or plate[1].isnumeric():
           return False
    
    for character in range(len(plate) - 1):
        actual = plate[character]
        next_one = plate[character + 1]
        if actual.isdigit() and next_one.isalpha():
            return False
        
        if actual == "0" and plate[character - 1].isalpha():
                return False

    return True





main()