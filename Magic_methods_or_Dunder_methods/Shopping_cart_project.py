class Cart:
    def __init__(self):
        self.lst = []

    def add(self,name):
        self.lst.append(name)

    def __len__(self):
        return len(self.lst)

    def __contains__(self,name):
        return name in self.lst

    def remove(self,name):
        if name in self.lst:
            self.lst.remove(name)
        else:
            print(f'{self.name} not in List')
            

    def __iter__(self):
        return iter(self.lst)

    def items(self):
        return self.lst

    def __str__(self):
        return f'{self.lst}'

    def __getitem__(self,index):
        return self.lst[index]
    
cart = Cart() # create object


cart.add('laptop') # add item in object
cart.add('mouse')
cart.add('keyboard')
cart.add('moniter')

for item in cart:
    print(item) # print all item one by one 

print('mouse' in cart) # print True if 'mouse' is in cart

print(len(cart)) # it print length

cart.remove('mouse') # it remove one item 'mouse'

print(cart) #it print all item 

print(cart[2]) # it print 'moniter'
