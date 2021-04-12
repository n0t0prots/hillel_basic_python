from datetime import datetime, date

den = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year(format 1967): '))
try:
    print(date(year, month, den))
except:
    print('Wrong date!')