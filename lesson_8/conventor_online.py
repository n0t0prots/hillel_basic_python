import argparse
from datetime import timedelta, datetime
import requests
from pprint import pprint


def responser():
    url = 'https://api.exchangerate.host/convert'
    fr = argsdict['fr']
    to = argsdict['to']
    amount = argsdict['amount']
    finance.append(['date', 'fr', 'to', 'rate ', 'result'])
    for date in daylist:
        pars = {'from': fr, 'to': to, 'amount': amount, 'date': date}
        response = requests.get(url, params=pars)
        data = response.json()
        finance.append([data['date'], fr, to, amount, data['info']['rate'], data['res']])


def date_of_user():
    user_date = argsdict['start_date']
    start_date = datetime.strptime(user_date, '%Y-%m-%d')
    if start_date > today_date:
        start_date = today_date
    return start_date


def make_req():
    tempdate = date_of_user()
    while tempdate <= today_date:
        daylist.append(tempdate.date())
        tempdate += timedelta(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Conventor online', description="Currency at your time")
    parser.add_argument('fr', default='USD')
    parser.add_argument('to', default='UAH')
    parser.add_argument('amount', default=100)
    parser.add_argument('--start_date', default=str(datetime.now().date()), nargs='?')
    args = parser.parse_args()
    argsdict = vars(args)
    today_date = datetime.now()
    finance = []
    daylist = []
    date_of_user(), make_req(), responser()
    pprint(finance)
