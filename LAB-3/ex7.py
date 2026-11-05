def filter_and_sort_products(products,max_price, category, sort_by):
    filtered_products = [
        product for product in products
        if product['price'] <= max_price
        and (category is None or product['category'] == category)
    ]

    if sort_by == "price_asc":
        return sorted(filtered_products, key=lambda x: x['price'])
    elif sort_by == "price_desc":
        return sorted(filtered_products, key=lambda x: x['price'], reverse=True)
    elif sort_by == "rating_asc":
        return sorted(filtered_products, key=lambda x: x['rating'])
    elif sort_by == "rating_desc":
        return sorted(filtered_products, key=lambda x: x['rating'], reverse=True)
    else:
        return filtered_products


products = [
    {"name": "Product A", "price": 10, "category": "Electronics", "rating": 4.5},
    {"name": "Product B", "price": 20, "category": "Clothing", "rating": 4.0},
    {"name": "Product C", "price": 15, "category": "Electronics", "rating": 3.5},
    {"name": "Product D", "price": 30, "category": "Clothing", "rating": 5.0},
]

result = filter_and_sort_products(products, 25, "Electronics", "price_asc")

print(result)