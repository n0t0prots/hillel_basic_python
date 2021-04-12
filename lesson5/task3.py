a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
fig = input('If square enter Y, If triangle enter N ')

square_1 = a * b
triangle_1 = a * b / 2
if fig == 'Y':
    print('Area of square: ', square_1)
elif fig == 'N':
    print('Area of triangle: ', triangle_1)
else:
    print('You enter the wrong!')