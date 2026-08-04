def main():
    time = input("What time is it? ")
    hora_float = convert(time)
    if hora_float >= 7 and hora_float <= 8:
        print("breakfast time")
    elif hora_float >= 12 and hora_float <= 13:
        print("lunch time")
    elif hora_float >= 18 and hora_float <= 19:
        print("dinner time")
    else:
        print("")



def convert(time):
    time = time.split(":")
    hora1= int(time[0])
    hora2= int(time[1])
    hora2 = float(hora2 / 60)
    horafinal = hora1 + hora2
    return horafinal


if __name__ == "__main__":
    main()