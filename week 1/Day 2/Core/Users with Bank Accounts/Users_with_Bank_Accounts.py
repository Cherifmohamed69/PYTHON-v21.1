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

# user class :

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def transfer_money(self, amount, other_user):
        self.account.balance = self.account.balance - amount
        other_user.account.balance = other_user.account.balance + amount
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")
        return self

    def display_account_info(self):
        print(f"Name: {self.name}, {self.account.display_account_info()}")
        return self

mohamed =User("mohamed","cherif@gmail.com")
ayoub = User("ayoub","ayoub@dogmail.com")



mohamed.account.deposit(100)
mohamed.display_account_info()
ayoub.account.deposit(500)
mohamed.transfer_money(500,user2)
ayoub.account.deposit(100).withdraw(50).display_account_info()