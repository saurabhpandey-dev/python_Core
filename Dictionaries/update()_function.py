##the .update() method updates the key-value pairs with the key-value pairs of
##another dictionary. If they have keys in common, their values are overwritten.
##
##In this example, we are updating the pizza dictionary. The price key exists
##in both of them, so its value will be replaced with 15.
##
##But total_time is new, so it will be added to the pizza dictionary as a new
##key-value pair.


pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(pizza, '\n')

pizza.update({'price':15,'time':15})

print('updated dict :- ')
print(pizza)

#the update() function is use for two purpose 1 :- update the value
 #                                            2 :- add new key value pair   
