# Python me jab hume yeh nahi pata hota ki user function call karte waqt
# kitne arguments dega, tab hum in dono ka use karte hain. Yahan args aur 
# kwargs sirf naam hain (aap unki jagah *naam ya **details bhi likh sakte 
# hain), asli jaadu single star (*) aur double star (**) ka hai.

# *args 
# (Non-Keyword / Positional Arguments)Kab use karein?
# Jab aapko sirf values bhejni hon, bina kisi naam ke (jaise numbers ki list 
# ya naam ki list).

# Piche kya hota hai? 
# Python un saari values ko pakadkar ek Tuple (immutable list) me pack kar 
# deta hai.

class Calculator:

    def add(self, *args):
        print(f'value passed : {args}')  # here print all values
        print(f'type is : {type(args)}') # and here is type of args
        print(f'sum os {sum(args)}','\n') # here is the sum

calc = Calculator()

calc.add(1,9,4,6,2,3,4,7,2,6) #ans is 44 and no matter how many argument you pass

calc.add(1,9,4,6,2,3)