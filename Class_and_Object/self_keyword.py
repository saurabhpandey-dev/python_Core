class Students:
    ...

    
    def display(self):
        print("name :",self.name)
        print("age :",self.age)


student = Students()
student.name=input('Enter the name : ')
student.age=int(input('Enter the age : '))

student.display()


##self represents the specific instance of a class. It is used as a reference
##to access or modify the object's properties and methods.
##
##What self Does Because a single class can be used to create thousands of
##different objects (e.g., thousands of unique Dog objects), self acts as a
##direct link between the method and the specific object you are working with.
##
##Identifies the object: It tells the program which specific instance's data to
##access or alter.Keeps data separate: It ensures that one object's data
##(like dog1.name) does not overwrite another's (dog2.name).
##
##Key Rules & Concepts
##
##It is not actually a keyword: Contrary to popular belief, self is
##simply a naming convention, not a built-in language keyword. You could
##technically name it this or even potato, but it is heavily discouraged by the
##coding community.
##
##Must be the first parameter: In Python, self must always be
##explicitly declared as the first parameter in class methods.
##
##Passed automatically: When you call a method on an object, Python automatically passes that object
##as the self argument behind the scenes.



class Dog:
    ...
##    def display(this):  # self is not a keyword,Contrary to popular belief
##        print(this.name)
##        print(this.age)
    def display(me):
        print(me.name)
        print(me.age)


dog = Dog()
dog.name= input("enter the name:")
dog.age=int(input("enter the age :"))

dog.display()
