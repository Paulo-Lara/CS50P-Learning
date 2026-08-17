#We use cycle for to eliminate each character in "vocales" (vowels)

word = input("Input: ").strip()
vocales = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for letra in vocales:
    word = word.replace(letra, "")

print(word ,end="")

