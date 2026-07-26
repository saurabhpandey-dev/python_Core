# Implicit conversion Python khud karta hai jab data loss ka risk na ho 
# (jaise int ko float me operation ke time). 

a = 10
b = 5.5

c = a + b

print(c) # it print  15.5 becouse python change data type internally
print(type(c))  # <class 'float'> 