# main.py

from saving import SavingsAccount
from current import CurrentAccount
from children import ChildrenAccount
from student import StudentAccount

def main():
    # Create different types of accounts
    savings = SavingsAccount("SA123", 1000)
    current = CurrentAccount("CA123", 2000)
    children = ChildrenAccount("CH123", 500)
    student = StudentAccount("ST123", 300)

    # Test deposits
    savings.deposit(100)
    current.deposit(200)
    children.deposit(100)
    student.deposit(50000)

    # Test withdrawals
    savings.withdraw(500)
    current.withdraw(500)
    children.withdraw(100)
    student.withdraw(1000)

    # Check balances
    print(f"Savings Account Balance: {savings.get_balance()}")
    print(f"Current Account Balance: {current.get_balance()}")
    print(f"Children Account Balance: {children.get_balance()}")
    print(f"Student Account Balance: {student.get_balance()}")

if __name__ == "__main__":
    main()
