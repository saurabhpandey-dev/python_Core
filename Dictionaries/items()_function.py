##The .items() method returns a view object with all the key-value pairs
##in the dictionary, including both the keys and the values.

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza.items())


##Iterating with For Loops: The most common use case for items() is looping
##through a dictionary to get both keys and values simultaneously via tuple
##unpacking.

##

##Dynamic Views: The dict_items object is a dynamic view, meaning that if you
##change, add, or delete elements in the original dictionary, the view updates
##automatically without requiring a second method call.

##

##Type Conversion: If you need an actual static list or indexable object rather
##than a view, you can cast it into a list using list(my_dict.items())
