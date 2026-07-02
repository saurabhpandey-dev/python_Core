# The setattr() function lets you create a new attribute or update an existing one dynamically.

class Student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    

stu1 = Student('Saurabh',23)

att_name = input('Enter the attribute name : ')
att_value = input('Enter the attribute value : ')

setattr(stu1,att_name,att_value)

for attr in dir(stu1):
    if not attr.startswith('__'):
        value=getattr(stu1,attr)
        print(f'{attr} : {value}')


