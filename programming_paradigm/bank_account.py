class BankAccount:

    def __init__(self, account_balance=0) -> None:
        self.account_balance = float(account_balance)

    def deposit(self, amount: float):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount: float):
        if self.account_balance >= amount:
            self.account_balance -= amount
        return self.account_balance

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
