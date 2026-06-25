##her i create two object and call each-other

class Dog:
    ...

    def display(self):
        print(self.name)
        print(self.age)

dog1 =Dog()
dog2 =Dog()

dog1.name=input("Enter the name for dog 1 :")
dog1.age=int(input('enter age :'))

dog2.name=input("Enter the name for dog 2 :")
dog2.age=int(input('enter age :'))

dog1.display()
dog2.display()
