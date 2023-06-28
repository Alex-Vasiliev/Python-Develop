# Розробіть клас BankAccount для представлення банківського рахунку.
# Додайте методи для зняття та поповнення коштів на рахунку.
# Використовуйте магічний метод __str__ для виведення інформації про рахунок.

class BankAccount:
    def __init__(self, number_account, name_account, balance=0):
        self.number_account = number_account
        self.name_account = name_account
        self.balance = balance

    def deposit_cash(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance} units.")

    def withdraw_cash(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdraw {amount} units. Current balance: {self.balance} units.")

        else:
            print(f"Insufficient funds. Withdrawal canceled. Balance {self.balance} units.")

    def __str__(self):
        return f"Name account: {self.name_account}\nNumber account: {self.number_account}\nBalance: {self.balance}"


client1 = BankAccount(3498761209, "Chuna Brouwn")

print(client1)

operations = True
while operations:
    operations = int(input("What operations do you want to do?\n"
                           "1 - Deposit cash\n"
                           "2 - Withbraw_cash\n"
                           "3 - Finish the job\n"
                           "Enter the number: "))
    if operations == 1:
        deposit = int(input("Enter the top-up amount: "))
        client1.deposit_cash(deposit)
    elif operations == 2:
        withbraw = int(input("Enter the withdrawal amount: "))
        client1.withdraw_cash(withbraw)
    elif operations == 3:
        print("The work is completed")
        operations = False

    else:
        print("Incorrectly entered value")
        continue
