#This one took a while, but I used a lot of functions that I didn't use before, but after debugging for hours, it worked
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
        Rn = plate[character]
        next = plate[character + 1]
        if Rn.isdigit() and next.isalpha():
            return False

        if Rn == "0" and plate[character - 1].isalpha():
                return False

    return True





main()
