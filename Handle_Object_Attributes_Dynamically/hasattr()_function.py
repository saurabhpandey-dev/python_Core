#There is also hasattr(). Before you do something with an attribute or delete it, it's a good practice 
#to check if it exists. That's what hasattr() lets you do. It checks if an attribute exists and 
#returns True or False based on the result.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
stu1 = Student('saurabh',23)

print(hasattr(stu1,'name')) 
print(hasattr(stu1,'age'))
print(hasattr(stu1,'phone'))