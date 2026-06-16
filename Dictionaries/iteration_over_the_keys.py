products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.keys():
    print(product)

    #    OR

##for product in products:
##    print(product)


##This works exactly the same for .keys() if you need to iterate over the keys
##of a dictionary. You just need to iterate over products.keys() or products
##directly, and assign a descriptive name for the loop variable
