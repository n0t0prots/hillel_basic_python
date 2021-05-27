from random import randint

listOrigin = [randint(1, 10) for i in range(10)]
listMask = []
for i in listOrigin:
    if int(i) % 2 == 0:
        listMask.append(i)
    else:
        listMask.append(0)

print(listOrigin)
print(listMask)