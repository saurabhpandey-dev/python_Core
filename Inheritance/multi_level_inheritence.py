class A:
    a = 'A data'
    
class B(A):  # B inherit A
    b = 'B data'

class C(B): # C inheri A and B
    c = 'C data'
    
obj0 = A()
obj1 = B()
obj2 = C()

print(obj0.a) 
# print(obj0.b) # error becouse A is supar parent class
# print(obj0.c)

print(obj1.a)
print(obj1.b)
# print(obj1.c) # error becouse B is mid parent class

print(obj2.a)
print(obj2.b)
print(obj2.c)