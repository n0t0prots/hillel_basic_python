list_1 = ['a', 'b', 'c', 'd', 'e']
key = []

for i in enumerate(list_1):
    key.append(i)

list_2 = {x: y for x in range(5) for y in list_1[x]}
print(list_2)