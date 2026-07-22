class Vahical:
    def start_engine(self):
        print('Engine is started ready to GO!!')
    
    def horn(self):
        print('All vahical have a Horn BEEP BEEP #')

class Bike(Vahical):
    def horn(self):
        print('Bike have a Horn Peep Peep!#!')

class Car(Vahical):
    def horn(self):
        print('Car have a Horn Pomp Pomp ->>')
    
car = Car()
bike = Bike()

bike.start_engine()
bike.horn()

car.start_engine()
car.horn()