##The .pop() method removes the key-value pair with the key that you specify as
##the first argument and returns its value. If the key doesn't exist, it returns
##the default value that you specify as the second argument. If the key doesn't
##exist and you don't pass a default value, a KeyError is raised



pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza,'\n')

pizza.pop('price',8.9)

print('price and its value is got deleted :- ')
print(pizza)
