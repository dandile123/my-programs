class BankAccount:
    # class variable
    ROI = 10.5

    # constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # display details
    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    # deposit amount
    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt

    # withdraw amount
    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
        else:
            print("Insufficient balance")

    # calculate interest
    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


# creating multiple objects
Obj1 = BankAccount("Ganesh", 5000)
Obj2 = BankAccount("Rahul", 8000)

# operations for first object
Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
Obj1.Display()

print("----------------------")

# operations for second object
Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
Obj2.Display()
