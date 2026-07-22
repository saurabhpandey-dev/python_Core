# Python is a dynamically typed language that adheres to the philosophy: 
# "If it walks like a duck and quacks like a duck, it's a duck.". 

# You do not need objects to share an inheritance tree; they just need to 
# share the same method names.


class paytm:
    def pay(self,amount):
        print(f'paymant: {amount} done by paytm')

class gpay:
    def pay(self,amount):
        print(f'payment: {amount} done by gpay')
    
def transaction(gateway,amount):
    gateway.pay(amount)

transaction(gpay(),2500)