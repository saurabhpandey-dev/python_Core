##The .get() method retrieves the value associated with a key.
##It's similar to the bracket notation that we just used, but its advantage
##is that you can set a default value, so you won't get an error if the key
##doesn't exist

pizza = {
         'name': 'Margherita Pizza',
         'price': 8.9,
         'calories_per_slice': 250,
         'toppings': ['mozzarella', 'basil']
         }

##print(pizza.get('teast')) #it's return none

print(pizza.get('test','not found')) # here i create the default value
                                    # when key is not found 
