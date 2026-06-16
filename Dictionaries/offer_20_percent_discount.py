products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


for product,price in products.items():
    print(product,price)

print()
##for product, price in products.items():
##    products[product] = round(price * 0.8)
##    print(product,price)
    
for product, price in products.items():
    print(product,price*(0.8))
