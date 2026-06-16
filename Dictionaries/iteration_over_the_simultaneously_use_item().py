products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.items():
    print(product)

##This works exactly the same for key-value pairs if you need to iterate
##over the keys and their corresponding values simultaneously.
##You just need to iterate over products.items().
##Now you get individual tuples with the keys and their corresponding
##values.
