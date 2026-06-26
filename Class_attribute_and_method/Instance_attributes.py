##Instance attributes are unique to each object created from a class, and
##you usually set them with the __init__ method.

class Students:
    def __init__(self,name,age):
        self.name=name  # instance attributes
        self.age=age

    def display(self):
        print(f'Student name :- {self.name} \n Age :- {self.age}')


student1 = Students('Saurabh',23)
student2 = Students('Ganguli',22)

student1.display()
student2.display()
