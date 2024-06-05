# student account with a withdrawal limit of 2,000 and deposit limit of 50,000 per deposit.

from account import Account

class StudentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 2000
        self.deposit_limit = 50000

    def deposit(self, amount):
        if amount <= self.deposit_limit:
            super().deposit(amount)
        else:
            print(f"Cannot deposit more than {self.deposit_limit} per transaction")

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw more than {self.withdrawal_limit} per transaction")
