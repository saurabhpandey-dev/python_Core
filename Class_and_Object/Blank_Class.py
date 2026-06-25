##Classes and objects work hand in hand to organize and manage data.
##You build a class to define shared behavior, then create objects that
##use those behaviors.

##In other words, a class is like a blueprint or template you use to create
##objects with.
##
##Let's look at what classes are, and how to use them to create objects.
##
##To create a class, you use the class keyword followed by the name of the
##class and a colon. Then within the class, you can add an initializer,
##along with any attributes and methods.
##
##Attributes are like variables within a class, and are used to store data.
##Methods are functions defined within a class, and are the actions objects
##created with a class can perform.

##class ClassName is made up of the class keyword to create a class, followed
##by the name of the class, here called ClassName. It is common in Python to
##use the PascalCase convention when naming classes.
##
class Myclass:
    ...


def insdata():
    x=input('Enter the name :')
    y=int(input('Enter the age : '))
#
    obj= Myclass()  #  here is the object created
#
    obj.name = x
    obj.age = y

    print(obj.name)
    print(obj.age)


insdata()

