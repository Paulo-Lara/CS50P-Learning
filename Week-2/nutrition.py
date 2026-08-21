#Probably the easiest one (from this week) so far, I remember seeing dictionaries or something similar in another week.
fruta = input("Item: ").lower()

lista = {
    "banana": 110,
    "apple": 130,
    "avocado": 50,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 90,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,

}
if fruta in lista:
    print(f"{lista[fruta]}")
else:
    print("")