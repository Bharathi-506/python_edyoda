class Account:
    def __init__(self, title=None, balance= 0):
        self.title = title
        self.balance = balance

    def deposit(self):
        amount = float(input("Enter the amount to be deposit:"))
        self.balance = self.balance + amount
        print("\n Amountdeposited :",amount)


    
    def withdrawal(self):
        amount = float(input("Enter amount to be withdrawal:"))
        self.balance = self.balance - amount 
        print("\n Amount withdrew :",amount)
    
        
    def getBalance(self):
        return self.balance
        

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, intrestRate=0):
            super().__init__(title, balance)
            self.intrestRate = intrestRate
    
    def interestAmount(self):
        print ("Intrestamount:", self.balance* self.intrestRate/100)

A = Account("Asish",2000)

A.deposit()
print(A.getBalance())

A. withdrawal()
print(A.getBalance())
        



S = SavingsAccount("Ashish", 2000, 5 )
S.interestAmount()