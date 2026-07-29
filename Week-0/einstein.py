"""Here we ask the user for mass (in Kg) and we automatically enter the value of speed
light (300000000 m/s), then it is going to output the result of Energy in Joules.
"""
speedoflight = 300000000
c = speedoflight ** 2

m = int(input("What is your kilogram (mass) input? "))

E = m*c
print("Your final value is",E)