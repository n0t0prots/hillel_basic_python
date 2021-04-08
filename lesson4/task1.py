import math
x = input('Quantity km in a first day?')
y = input('How many kilometres  have run in total?')
day = (int(y)/int(x))**(10/11)
print(math.ceil(day))
