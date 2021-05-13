def football_points():
    w = int(input('Number of wins:'))
    d = int(input('Number of draws:'))
    l = int(input('Number of loses:'))
    counter = w * 3 + d * 1 + l * 0
    return counter

print(football_points())