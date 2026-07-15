class Parent1:
    p1_data = 'Parent1 data'

class Parent2:
    p2_data = 'Parent2 data'

class Child1 (Parent1): # inherite Parent1 class
    c1_data = 'Child One'

class Child2 (Parent1,Parent2): # inherite Parent1 and Parent2 class
    c2_data = 'Child Two'
    
class Child3 (Parent1): # inherite Parent1 class
    c3_data = 'Child Two'
    
obj1 = Parent1()
obj5 = Parent2()
obj2 = Child1()
obj3 = Child2()
obj4 = Child3()

print(obj1.p1_data)
print(obj5.p2_data)

print(obj2.c1_data)

print(obj3.c2_data)
print(obj3.p1_data)
print(obj3.p2_data)

print(obj4.c3_data)
print(obj4.p1_data)
