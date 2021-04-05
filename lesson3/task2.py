num = input('Enter the number:')
num_1 = list(str(num).split('.'))
print('Decimal part is:', int(num_1[1]))
num_2 = int(num_1[1]) // 10
print('First digit after point is:', num_2)
