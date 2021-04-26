def forecast_of_weather():
    import requests
    import datetime
    API_KEY = 'f9ada9efec6a3934dad5f30068fdcbb8'
    name_of_city = 'Odessa'
    cnt = 5
    request = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?', params={'q': name_of_city, 'cnt': cnt, 'appid': API_KEY})
    data = request.json()
    date_start = datetime.datetime.now().strftime('%d-%m-%Y') + '-' + str(name_of_city) + ' ' + str(cnt) + 'days-forecast.txt'
    weather_f = open(date_start, 'w')
    weather_f.write('date: \t\t day:\t night:\t feels like(day):\t feels like(night): \n')
    for data_list in data['list']:
        weather_f.write(str(datetime.datetime.fromtimestamp(data_list['dt']).strftime('%d-%m-%Y')) + '\t')
        weather_f.write(str(data_list['temp']['day']) + '\t')
        weather_f.write(str(float(data_list['temp']['night'])) + '\t\t')
        weather_f.write(str(data_list['feels_like']['day']) + '\t\t\t\t')
        weather_f.write(str(data_list['feels_like']['night']) + '\n')
    weather_f.close()


forecast_of_weather()
