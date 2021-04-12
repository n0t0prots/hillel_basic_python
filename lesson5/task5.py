a = int(input('Enter the side of square: '))
t = []


def square():
    per = a * 4
    t.append(per)
    sq = a ** 2
    t.append(sq)
    diag = a * 2 ** (1 / 2)
    t.append(round(diag))
    tp = tuple(t)
    print(tp)


square()
