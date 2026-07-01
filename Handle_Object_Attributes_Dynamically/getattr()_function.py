#getattr() makes it possible to read an attribute from an object when you
#don't know its name until runtime. If the attribute doesn't exist,
#it raises an AttributeError, unless you provide a default value.


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age



student1 = Student('saurabh',23)
student2 = Student('Ganguly',22)


print(getattr(student1,'name'))
print(getattr(student1,'age'))
        
print(getattr(student2,'name'))
print(getattr(student2,'age'))




