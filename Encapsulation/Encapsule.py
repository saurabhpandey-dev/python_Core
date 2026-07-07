# Encapsulation is the bundling of the attributes and methods of an 
# object into a single unit, the class.

# With encapsulation, you can hide the internal state of the object behind
# a simple set of public methods and attributes that act like doors. Behind those doors are private attributes
# and methods that control how the data changes and who can see it.


class Wallet:
   def __init__(self, balance):
       self.__balance = balance # Private attribute

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount # Remove from the balance safely

   def get_balance(self):
        return self.__balance
   
   def validate(self,amount):
       if amount<0:
           raise ValueError('Amount must be positive')
    
# account = Wallet(500)
# print(account.get_balance()) # AttributeError: 'Wallet' object has no attribute '__balance'

acct_one = Wallet(100)
acct_one.deposit(50)
print(acct_one.get_balance()) # 150

acct_two = Wallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # 422

acct_two.deposit(150)
print(acct_two.get_balance()) # 572

# you can make deposit() and withdraw() public methods, and you hide the balance under the _balance attribute