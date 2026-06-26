class Books:
    def __init__(self,name):
       self.name=name

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return str(self.name)

    
book1 = Books(['the tower of Woks','Biography of Great Saurabh G. Pandey'])
book2 = Books(['the Malik','Utpaat'])
print(book1)
print(book2)
print(len(book1))
print(len(book2))

