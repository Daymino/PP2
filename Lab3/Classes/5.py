class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
            else:
                print("Insufficient funds. Withdrawal not allowed.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")


account = Account("John Doe", 1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(800)
account.deposit(1000)
account.withdraw(1200)