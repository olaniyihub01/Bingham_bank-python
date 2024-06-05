# children account with an interest rate of 0.7% and zero withdrawal

from account import Account

class ChildrenAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.007

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * self.interest_rate
        print(f"Interest added, new balance is {self._balance}")

    def withdraw(self, amount):
        print("Withdrawals are not allowed from a Children's account")
