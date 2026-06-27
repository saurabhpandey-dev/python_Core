class Books:
    def __init__(self):
        self.lst = []
        self.current = 0

    def add (self,name):
        self.lst.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.lst):
            raise StopIteration
        result = self.lst[self.current]
        self.current+=1
        return result


book = Books()

book.add('saurabh')
book.add('ganguly')
book.add('pandey')

for i in book:
    print(i)
        
