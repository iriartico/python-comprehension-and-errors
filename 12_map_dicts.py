items = [
    {
        'product': 'shirt',
        'price': 100
    },
    {
        'product': 'pants',
        'price': 250
    },
    {
        'product': 'shorts',
        'price': 30
    }
]

prices = list(map(lambda item: item['price'], items))

# new_items = [item | {'taxes': item['price'] * .19} for item in items]
new_items = list(map(lambda item: item | {'taxes': item['price'] * .19}, items))
print(new_items)
print(items)
