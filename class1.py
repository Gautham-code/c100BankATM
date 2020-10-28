class ATM(object):

    def __init__(self,company,Transaction_limit):
        self.company = company
        self.Transaction_limit = Transaction_limit
    
    def amount(self):
        print("Amount = 2000")

    def Debited(self):
        print("Given")
    
Icici = ATM("ICICI",8000)

print(Icici.amount())
print(Icici.Debited())
