class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
print = "========================================================"
# create acconts
account1 = BankAccount()
account2 = BankAccount()

# Account 1 transactions
account1.deposit(500)
account1.withdraw(300)
account1.display_account_info()
account1.yield_interest()
account1.display_account_info()

# Account 2 transactions
account2.deposit(30)
account2.withdraw(70)
account2.display_account_info()
account2.yield_interest()
account2.display_account_info()








