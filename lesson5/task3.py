a = int(input('enter a:'))
b = int(input('enter b:'))
fig = input('for quadratic - Y, triangle - N ')

qdr = a * b
tria = a * b / 2
if fig == 'N':
    print('square tria: ', tria)
elif fig == 'Y':
    print('square qdr: ', qdr)
else:
    print('Wrong enter')