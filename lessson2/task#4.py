year_number = int(input('Enter the year:'))
if (year_number % 4) == 0 and (year_number % 100) != 0:
    print('Yes!')
elif year_number % 400 == 0:
    print('Yes!')
else:
    print('No!')