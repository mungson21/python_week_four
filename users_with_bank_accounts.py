class BankAccount:
    # class attributes
    balance = []
    int_rate = 0.01
    def __init__(self, int_rate = 0.01, account_balance = 0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.account_balance = account_balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.account_balance -= 5
            return self
        else:
            self.account_balance -= amount
            return self
        return self
    def display_account_info(self):
        print('Balance: ' + str(self.account_balance))
    def yield_interest(self):
        if self.account_balance > 0:
            x = self.account_balance
            x *= 0.01
            self.account_balance += x
            return self
        else:
            pass

# Do not change anything in the BankAccount class.

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, account_balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print('User: ' + self.name + ', ' + 'Balance: ' + str(self.account.account_balance))

mike = User("Mike", "mikey@python.net")
miguel = User("Miguel", "miguel@python.net")

mike.make_deposit(200).make_withdrawal(50).display_user_balance()
miguel.make_deposit(200).make_deposit(100).make_withdrawal(75).display_user_balance()

