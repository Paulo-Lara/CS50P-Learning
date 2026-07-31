#The logic goes:
#Input asking for the operation
#Then it splits() the operation into three different characters which are x, y and z.
#We convert both x and z into float
#Then I write if and elif to detect the symbol in y
#Then I print the whole thing with one decimal (:.1f)

operacion = input("Calculate anything! ")
operacion = operacion.split()

x = float(operacion[0])
y = operacion[1]
z = float(operacion[2])

calculation = 0

if y == "+":
    calculation = x + z
elif y == "-":
    calculation = x - z
elif y == "*":
    calculation = x * z
elif y == "/" and z == 0:
    raise ValueError("You can't divide by 0!!")
elif y == "/":
    calculation = x / z


print(f"{calculation:.1f}")