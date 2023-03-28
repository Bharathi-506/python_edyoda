class Account:
    def __init__(self,Title,Balance):
        self.Title = Title
        self.Balance = Balance
        print(f"""Title{self.Title}
        Balance{self.Balance}""")
class Savings_Account:
    def __init__(self,Title, Balance, Intrestrate):
        self.Title = Title
        self.Balance = Balance
        self.Intrestrate = Intrestrate
        print(f"""Title{self.Title}
        Balance{self.Balance}
        Intrestrate{self.Intrestrate}""")
A = Account("  Asish", 1000)
print(A)
S = Savings_Account("  Asish", 1000, 5)
print(S)
