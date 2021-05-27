x = input('input start length:')
y = input('input length to find a day:')
x = float(x)
y = float(y)
day = 1
while x < y:
    x = x + x / 10
    day = day + 1
print("Need:", day)
