##the .popitem() method removes the last inserted item.

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza,'\n')

pizza.popitem()

print(' last key topping and its value is got deleted :- ')
print(pizza)
