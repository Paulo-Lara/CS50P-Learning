#Logic behind this one was really cool!
due = 50

coins = [25, 10, 5]
owed = 0
while due > 0:
    print("Amount Due:",due)
    monedas = int(input("Insert coin: "))
    monedas = int(monedas)
    if monedas in coins:
        due = due - monedas
if due <= 0:
        owed = due *-1
        print("Change Owed:",owed)