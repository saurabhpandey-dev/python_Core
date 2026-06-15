##Because dict_items does not support standard sequence indexing (like [0]),
##you must convert it to a standard list first if you want to extract specific
##index entries.

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

lst = list(pizza.items())
print(lst,'\n')

print(lst[1])
