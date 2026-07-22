from abc import ABC, abstractmethod

class gateway(ABC):
    
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process(self):
        pass 

class UPI(gateway):
    def authenticate(self):
        print('UPI use Authenticating via PIN...')
    
    def process(self):
        print('Scan the QR code, Enter amount, enter PIN done.')

class Card(gateway):
    def authenticate(self):
        print('Enter details of card')
    
    def process(self):
        print('tap to machine,enter details, enter amount, enter the pin code ')

person1 = UPI()

person1.authenticate()
person1.process()

person2 = Card()

person2.authenticate()
person2.process()