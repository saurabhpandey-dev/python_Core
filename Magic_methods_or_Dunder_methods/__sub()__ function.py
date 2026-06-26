class Math:
    def __init__(self,a):
         self.a=a
         

    def __sub__(self,other):
        return self.a-other.a

math1 = Math(2)
math2 = Math(5)

print(math1-math2)
