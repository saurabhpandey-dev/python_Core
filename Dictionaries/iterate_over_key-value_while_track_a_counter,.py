products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

##for product in enumerate(products.items()):
##    print(product)



for index, product in enumerate(products.items(), 1):
    print(index, product)
##if you need to iterate over the key-value pairs while keeping track of a
##counter, you can call the enumerate() function. This counter essentially
##acts as a sort of "index" or "count" for that element within the loop.
##
##The function returns an enumerate object, which assigns an integer to each
##key-value pair, like a counter. You can start the counter from any number,
##but by default, it starts from 0.
##But the enumerate() function also assigns an integer to each key, so we get
##tuples with the integer and the key.
