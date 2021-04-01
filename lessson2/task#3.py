vasiliyspeed = int(input('Enter current Vasiliy speed in(km/h): '))
vasiliyhours = int(input('Enter hours of ride: '))
vasiliypos = abs(vasiliyhours * vasiliyspeed)
if int(vasiliyspeed)<0:
    print('Vasiliy drive back')
elif vasiliypos > 100:
    print('Vasiliy has arrived')
else:
    print('Stop mark: ', int(vasiliypos))
