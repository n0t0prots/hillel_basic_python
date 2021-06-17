win = int(input('Enter the number of wins: '))
draw = int(input('Enter the number of draws: '))
loss = int(input('Enter the number of defeats: '))


def result(w, d, l):
    list = [w * 3, d, l * 0]
    return sum(list)


print(result(win, draw, loss))