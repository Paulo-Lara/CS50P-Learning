#Definimos la primera variable, convert y le asignamos texto
def convert(texto):
    #Utilizamos .replace para convertir las caras de emojis a los emojis
    emojiconvertido = texto.replace(":)", "🙂").replace(":(", "🙁")
    #Regresamos el resultado
    return emojiconvertido

#Definimos la segunda variable main
def main():
    #Pedimos el texto con emoji
    emoji = input()
    #Mezclamos la función de convert con el input emoji
    final = convert(emoji)
    #Lo imprimimos
    print(final)
    #Colocamos main para que funcione toda la rama main
main()
