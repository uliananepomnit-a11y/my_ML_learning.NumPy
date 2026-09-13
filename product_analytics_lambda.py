products = [
    {'name': 'Smartphone', 'price': 50000, 'category': 'Electronics'},
    {'name': 'Laptop', 'price': 90000, 'category': 'Electronics'},
    {'name': 'Python textbook', 'price': 15000, 'category': 'Books'},
    {'name': 'Novel "1984"', 'price': 5000, 'category': 'Books'}
]
def average_price_for_each_category(products):
    unique_products = set(x['category'] for x in products)
    dictionary = {}
    for i in unique_products:
        filtered = list(filter(lambda a: a['category'] == i, products))
        prices = [b['price'] for b in filtered]
        average_prices = sum(prices) / len(prices)
        dictionary[i] = average_prices
    return dictionary
print(f'Average price for each category: {average_price_for_each_category(products)}')