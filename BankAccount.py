class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f'name: {self.name}')
        print(f'balance: {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


bankAccount = BankAccount("konto1", 58)
bankAccount.display()
bankAccount.withdraw(80)
bankAccount.display()
bankAccount.deposit(120)
bankAccount.display()
