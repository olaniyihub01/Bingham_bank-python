# savings_account that gains interest of 0.5% per deposit and a withdrawal limit of 700,000

from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * self.interest_rate
        print(f"Interest added, new balance is {self._balance}")

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw more than {self.withdrawal_limit}")
