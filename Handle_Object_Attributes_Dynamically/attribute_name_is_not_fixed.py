#In this case, if the user types in name, they see Saurabh, and if they
#type in age, they see 30. And if they type something that doesn't exist
#in the class like email, they see 'Attribute not found'.

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


stu1 = Student('saurabh',22)

attri = input('Enter the attribute name :- ')

print(getattr(stu1,attri,'Attribute not found!'))
