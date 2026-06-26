##Class attributes, on the other hand, belong to the class itself and are
##shared by all instances of that class.
##
##To access an attribute, you use dot notation.

class Students:

    college = 'Kashi Institute of Technology' # class attribute

    def __init__(self,name,course):
        self.name=name
        self.course=course

    def display(self):
        print(f'{self.college}')
        print(f'Name : {self.name}\nCourse : {self.course}')

student = Students('Saurabh','Mca')
student2 = Students('Ganguli','Mca')

    
student.display()
student2.display()
