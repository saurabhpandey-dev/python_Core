# **kwargs (Keyword Arguments)Kab use karein? 
# Jab aapko value ke sath-sath uska ek naam (key) bhi bhejna ho 
# (jaise age=25, city='Delhi').

# Piche kya hota hai? 
# Python in sabhi name-value pairs ko ek Dictionary me pack kar deta hai

class Student:

    def show(self,**kwargs): # **kwargs is only take and return dict 
        print(f'Name : {kwargs['name']}')
        print(f'age : {kwargs['age']}')
        print(kwargs)

person = Student()

person.show(name='saurabh',age='23') # here print {'name': 'saurabh', 'age': '23'}
