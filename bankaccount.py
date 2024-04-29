class bankAccount:
    def __init__(self, accNumber, balance, dateOpened):
        self.accNumber = accNumber
        self.balance = balance
        self.dateOpened = dateOpened
    def deposit(self, value):
        self.balance += value
        return self.balance
    def withdraw(self, value):
        self.balance -= value
        return self.balance
    def drop(self, value):
        self.balance = 0
        return self.balance
accOne = bankAccount(1, 1515, "10/01/1987")
transaction = input("Enter transaction: ")
bank = transaction.split()
bank[1], bank[2] = int(bank[1]), int(bank[2])
if len(bank) == 3:
    if bank[1] == 1:
        if bank[0] == "dep":
            print(accOne.deposit(bank[2]))
        elif bank[0] == "wd":
            print(accOne.withdraw(bank[2]))
        elif bank[0] == "drop":
            print(accOne.drop(bank[2]))
        else:
            print("Invalid transaction")
    else:
        print("Invalid transaction")
else:
    print("Invalid transaction")