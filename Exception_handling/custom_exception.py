class InsufficientBalence(Exception):
    def __init__(self,balence,amount):
        self.balence = balence
        self.amount = amount
        super().__init__(f'balence {self.balence} is less then amount {self.amount}')
    
def withdraw(balence,amount):
    if amount>balence:
        raise InsufficientBalence(balence,amount)
    return f'amount: {balence - amount} left in balence account'

balence = 20000

print(withdraw(balence,21000))

# Built-in Exception class se inherit karke apni custom exception class 
# bana sakte ho — taaki specific error scenarios ke liye meaningful naam 
# aur extra data attach kar sako.