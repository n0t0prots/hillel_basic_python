import re
import csv

car_number = input('Enter your vehicle number: ')
car_number.replace('I', 'І', 2)

requests = r'^\w{2}\d{4}\w{2}'
match = re.search(requests, car_number)

if not match:
    print('ERROR')
else:
    print('Pass')
    with open('ua_auto.csv', newline='') as File:
        reader = csv.DictReader(File)

        for row in reader:
            if car_number[0:2] == row['Код 2004']:
                print('2004 for', row['Регіон'])
                break
            elif car_number[0:2] == row['Код 2013']:
                print('2013 for', row['Регіон'])
                break