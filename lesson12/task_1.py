from datetime import datetime


class Bank_Account:

    def __init__(self, name, uuid, put_percent=0.01, get_percent=0.02, balance=0.0, tranzactions=[]):
        self.name = name
        self.uuid = uuid
        self.put_percent = put_percent
        self.get_percent = get_percent
        self.balance = balance
        self.tranzactions = tranzactions

    def put_money(self, money):
        self.balance += (1 - self.put_percent) * money
        self.tranzactions.append(
            str(datetime.now().strftime("%H:%M:%S")) + ", put: " + str((1 - self.put_percent) * money))

    def get_money(self, money):
        self.balance -= (1 - self.get_percent) * money
        self.tranzactions.append(
            str(datetime.now().strftime("%H:%M:%S")) + ", get: " + str((1 - self.get_percent) * money))

    def display_balance(self):
        print(self.balance)

    def display_tranzactions(self):
        for i in self.tranzactions:
            print(i)


TBA = Bank_Account("Tom Slider", "29012003")  # Tom's Bank Account
TBA.put_money(100)
TBA.get_money(10)
TBA.display_balance()
print()
TBA.display_tranzactions()