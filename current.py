# current account with no restrictions

from account import Account


class CurrentAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

# No restrictions, so no overrides where needed to be added
