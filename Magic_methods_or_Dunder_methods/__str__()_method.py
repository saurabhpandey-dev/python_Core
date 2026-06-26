##When you pass an object to the print() function, the str() constructor,
##or use it within f-strings, Python automatically calls this method under
##the hood to determine how the text should display.

class Students:

    def __init__(self,name,course):
        self.name=name
        self.course=course

    def __str__(self):
        return f'Student name : {self.name} \nCourse : {self.course}'


stu1 = Students('Saurabh','DevOps')
stu2 = Students('Ganguli','Cloud')

print(stu1) # the biggest advantage is using the __str__() you did not 
print(stu2)  # want to create the speacil display() function for print something

print(type(str(stu1)))
print(type(stu1)) # <class '__main__.Students'> if direct call

##class String:
##
##    def __init__(self,num):
##        self.num = num
##        
##    def __str__(self):
##        return f'{self.num}'
##
##
##num = int(input('enter the number'))
##
##s = String(num)
##
##print(s)
##print(str(s))
##print(type(str(s)))
