import uuid as uuid
import datetime


class BankAcc:
    def __init__(self, account_name: str, balance: float) -> True:
        self.account_name = account_name
        self.account_uuid = uuid.uuid4()
        self.balance = balance
        self.transactions = []


    def deposit(self, sum_increase):
        self.balance += sum_increase
        trans_datetime = datetime.datetime.now()
        self.transactions.append((trans_datetime.isoformat(sep=' '), 'deposit', str(sum_increase)))


    def withdrawal(self, sum_withdrawal):
        bank_comission = 0.01
        self.balance -= sum_withdrawal*(1 + bank_comission)
        trans_datetime = datetime.datetime.now()
        self.transactions.append((trans_datetime.isoformat(sep=' '), 'withdrawal', str(sum_withdrawal)))

    def balance_show(self):
        return self.balance

    def info_about(self):
        info = (self.account_name, self.account_uuid, self.balance)
        return info


notoprots = BankAcc('Artem Protsenko', 999.00)

notoprots.deposit(1488)
notoprots.withdrawal(228)
notoprots.deposit(1337)

print(notoprots.balance_show())
print(notoprots.transactions)
print(notoprots.info_about())