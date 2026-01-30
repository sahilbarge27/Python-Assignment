class BankAccount:
    ROI = 10.5   # class variable

    def _init_(self, name, amount):
        self.name = name
        self.amount = amount

    def Display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.amount)

    def Deposit(self):
        dep = float(input("Enter deposit amount: "))
        self.amount += dep
        print("Amount Deposited")

    def Withdraw(self):
        wd = float(input("Enter withdraw amount: "))
        if wd <= self.amount:
            self.amount -= wd
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print("Interest:", interest)


# Example usage
acc1 = BankAccount("Sahil", 1000)
acc1.Display()
acc1.Deposit()
acc1.Withdraw()
acc1.CalculateInterest()
acc1.Display()