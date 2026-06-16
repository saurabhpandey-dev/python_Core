##You can add an element to a set with the .add() method, and pass in the
##new element as argument.

s1= {1,2,3,4,5}
print(s1)
print(type(s1))

s1.add(6)
print(s1)

##If you try to add an element that is already in the set, only one will be
##kept. In this case, we already have the number 5 in the set:

s1.add(5)
print(s1)

##So the set will not change
