
class Cars:
    __slots__ = ['name','color']
    # if use __slots__ then python can't create the internal dictinoary

    def __init__ (self,modal,color):
        self.name=modal
        self.color=color

    def __str__(self):
        return f'your car {self.color} color {self.name}'


car1 = Cars('Defendar','Mocha Black')

print(car1)
print(car1.__dict__)#error becouse after using __slots__ does not allow to create
print(Cars.__dict__)# the attribute dynamiclly


car1.engine='2li' #error
car1.__dict__['Engine']= '2li' #error
setattr(car1, 'engine', '2li') #error


print(car1.__dict__) #error
