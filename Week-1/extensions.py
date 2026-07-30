
#I had to learn for i in range from 20 different tutorials just because I know I will need this in the future
#It did end up working out but the logic took ages to complete
#I know a little bit of C language so thats why it gave me an advantage to use the range function
archivo = input("File name: ")

punto = 0

for i in range(len(archivo)):
    if archivo[i] == ".":
        punto = i

final = archivo[punto :].lower().strip()

match final:
    case ".jpeg" | ".jpg":
        print("image/jpeg")

    case ".gif":
        print("image/gif")

    case ".png":
        print("image/png")

    case ".pdf":
        print("application/pdf")

    case ".txt":
        print("text/plain")

    case ".zip":
        print("application/zip")

    case ".bin":
        print("application/octet-stream")

    case _:
        print("application/octet-stream")

