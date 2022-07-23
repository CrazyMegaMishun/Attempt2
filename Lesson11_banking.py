import decimal
from datetime import date
import uuid
from decimal import Decimal


class BankAccount:
    def __init__(self, account_name, u_id, balance, transactions):
        decimal.getcontext().prec = 6
        self.account_name = account_name
        self.u_id = u_id
        self.balance = Decimal(balance)
        self.transactions = transactions

    def deposit(self, dep_sum):
        self.balance += dep_sum*Decimal(0.99)
        self.transactions.append([self.u_id,
                                  self.account_name,
                                  date.today().strftime("%Y-%m-%d"),
                                  dep_sum,
                                  self.balance])

    def cashout(self, out_sum):
        self.balance -= out_sum/Decimal(0.99)
        self.transactions.append([self.u_id,
                                  self.account_name,
                                  date.today().strftime("%Y-%m-%d"),
                                  out_sum,
                                  self.balance])

    def get_balance(self):
        print('Ваш баланс становить {} гривень'.format(self.balance))


Account1 = BankAccount('White', str(uuid.uuid4()), 1500.35, [])

Account1.deposit(Decimal(input('Скільки закинемо на рахунок: ')))
Account1.get_balance()

Account1.cashout(Decimal(input('Скільки знімемо з рахунку: ')))
Account1.get_balance()
