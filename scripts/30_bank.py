class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        dep = int(input("Enter amount to be deposited "))
        print(dep)
        self.balance = self.balance + dep
        print(f"Available balance is {self.balance}")

    def withdraw(self):
        wth = int(input("Enter amount to be withdrawn "))
        print(wth)
        if self.balance > wth:
            self.balance = self.balance - wth
            print(f"Available balance is {self.balance}")
        else:
            print("Insufficient funds")

nam = Account("Virappan", 3000)
print(f"Account holder is {nam.owner} and available balance is {nam.balance}")
nam.deposit()
nam.withdraw() 
