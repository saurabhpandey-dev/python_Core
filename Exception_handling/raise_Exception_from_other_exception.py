try:
    number = int('ABC')
except ValueError as v:
    print('enter the shi value')
    raise RuntimeError ('entered data is Char') from v
    