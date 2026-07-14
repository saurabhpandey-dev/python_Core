#a decorator is a function that modifies the functionalities of other functions,
# or classes, without changing their original code.

def company(func):
    def company_name():
        print('TATA MOTARS')
        func()
    return company_name

@company
def modal():
    print('SAFARI')
    
    
modal()