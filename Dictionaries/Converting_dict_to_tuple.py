pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

tup = tuple(pizza.items())
print(tup,'\n')

print(tup[1])
print(tup[0][1])
