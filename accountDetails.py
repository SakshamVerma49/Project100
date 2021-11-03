class BankDetails(object): 
    def __init__(self, name, accountNumber, accountBalance, debitCardNumber, creditCardNumber):
        self.name = name
        self.accountNumber = accountNumber
        self.accountBalance = accountBalance
        self.debitCardNumber = debitCardNumber
        self.creditCardNumber = creditCardNumber
    
    def withdrawl(self, amount):
        self.accountBalance = self.accountBalance - amount
        print("Amount Withdrawn! Current balance in your account is: ", self.accountBalance)

    def deposit(self, amount):
        self.accountBalance = self.accountBalance + amount
        print("Amount deposited, you're close to being rich now! Current balance in your account is: ", self.accountBalance)

Saksham = BankDetails("Saksham", 1234567890, 133, 1901232132014543, 1234567890123456)
Saksham.deposit(300)
Saksham.withdrawl(5)